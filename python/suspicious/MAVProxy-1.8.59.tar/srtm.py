class SRTMDownloader():
    """Automatically download SRTM tiles."""
    def __init__(self, server="terrain.ardupilot.org",
                 directory="SRTM3",
                 cachedir=None,
                 offline=0,
                 debug=False,
                 use_http=False):

        if cachedir is None:
            try:
                cachedir = os.path.join(os.environ['HOME'], '.tilecache', directory)
            except Exception:
                if 'LOCALAPPDATA' in os.environ:
                    cachedir = os.path.join(os.environ['LOCALAPPDATA'], '.tilecache', directory)
                else:
                    import tempfile
                    cachedir = os.path.join(tempfile.gettempdir(), 'MAVProxy', directory)

        # User migration to new folder struct (SRTM -> SRTM3)
        if directory == "SRTM3" and not os.path.exists(cachedir) and os.path.exists(cachedir[:-1]):
            print("Migrating old SRTM folder")
            os.rename(cachedir[:-1], cachedir)
        
        self.debug = debug
        self.offline = offline
        self.offlinemessageshown = 0
        if self.offline == 1 and self.debug:
            print("Map Module in Offline mode")
        self.first_failure = False
        self.server = server
        self.directory = "/" + directory +"/"
        self.cachedir = cachedir
        if self.debug:
            print("SRTMDownloader - server=%s, directory=%s." % (self.server, self.directory))
        if not os.path.exists(cachedir):
            mp_util.mkdir_p(cachedir)
        self.filelist = {}
        self.filename_regex = re.compile(
                r"([NS])(\d{2})([EW])(\d{3})\.hgt\.zip")
        self.filelist_file = os.path.join(self.cachedir, "filelist_python")
        self.min_filelist_len = 14500
        self.use_http = use_http

    def loadFileList(self):
        """Load a previously created file list or create a new one if none is
            available."""
        try:
            data = open(self.filelist_file, 'rb')
        except IOError:
            '''print("No SRTM cached file list. Creating new one!")'''
            if self.offline == 0:
                self.createFileList()
            return
        try:
            self.filelist = pickle.load(data)
            data.close()
            if len(self.filelist) < self.min_filelist_len:
                self.filelist = {}
                if self.offline == 0:
                    self.createFileList()
        except:
            '''print("Unknown error loading cached SRTM file list. Creating new one!")'''
            if self.offline == 0:
                self.createFileList()

    def createFileList(self):
        """SRTM data is split into different directories, get a list of all of
            them and create a dictionary for easy lookup."""
        global childFileListDownload
        global filelistDownloadActive
        mypid = os.getpid()
        if mypid not in childFileListDownload or not childFileListDownload[mypid].is_alive():
            childFileListDownload[mypid] = multiproc.Process(target=self.createFileListHTTP)
            filelistDownloadActive = 1
            childFileListDownload[mypid].start()
            filelistDownloadActive = 0

    def getURIWithRedirect(self, url):
        '''fetch a URL with redirect handling'''
        tries = 0
        while tries < 5:
                if self.use_http:
                    conn = httplib.HTTPConnection(self.server)
                else:
                    conn = httplib.HTTPSConnection(self.server)
                conn.request("GET", url)
                r1 = conn.getresponse()
                if r1.status in [301, 302, 303, 307]:
                    location = r1.getheader('Location')
                    if self.debug:
                        print("redirect from %s to %s" % (url, location))
                    url = location
                    conn.close()
                    tries += 1
                    continue
                data = r1.read()
                conn.close()
                if sys.version_info.major < 3:
                    return data
                else:
                    encoding = r1.headers.get_content_charset()
                    if encoding is not None:
                        return data.decode(encoding)
                    elif ".zip" in url or ".hgt" in url:
                        return data
                    else:
                        return data.decode('utf-8')
        return None

    def createFileListHTTP(self):
        """Create a list of the available SRTM files on the server using
        HTTP file transfer protocol (rather than ftp).
        30may2010  GJ ORIGINAL VERSION
        """
        mp_util.child_close_fds()
        if self.debug:
            print("Connecting to %s" % self.server, self.directory)
        try:
            data = self.getURIWithRedirect(self.directory)
        except Exception:
            return
        parser = parseHTMLDirectoryListing()
        parser.feed(data)
        continents = parser.getDirListing()
        
        # Flat structure
        if any(".hgt.zip" in mystring for mystring in continents):
            files = continents
            for filename in files:
                if ".hgt.zip" in filename:
                    self.filelist[self.parseFilename(filename)] = ("/", filename)
        else:
            # tiles in subfolders
            if self.debug:
                print('continents: ', continents)

            for continent in continents:
                if not continent[0].isalpha() or continent.startswith('README'):
                    continue
                if self.debug:
                    print("Downloading file list for: ", continent)
                url = "%s%s" % (self.directory,continent)
                if self.debug:
                    print("fetching %s" % url)
                try:
                    data = self.getURIWithRedirect(url)
                except Exception as ex:
                    print("Failed to download %s : %s" % (url, ex))
                    continue
                parser = parseHTMLDirectoryListing()
                parser.feed(data)
                files = parser.getDirListing()

                for filename in files:
                    self.filelist[self.parseFilename(filename)] = (
                                continent, filename)

                '''print(self.filelist)'''
        # Add meta info
        self.filelist["server"] = self.server
        self.filelist["directory"] = self.directory
        tmpname = self.filelist_file + ".tmp"
        with open(tmpname , 'wb') as output:
            pickle.dump(self.filelist, output)
            output.close()
            try:
                os.unlink(self.filelist_file)
            except Exception:
                pass
            try:
                os.rename(tmpname, self.filelist_file)
            except Exception:
                pass
        if self.debug:
            print("created file list with %u entries" % len(self.filelist))

    def getTile(self, lat, lon):
        """Get a SRTM tile object. This function can return either an SRTM1 or
            SRTM3 object depending on what is available, however currently it
            only returns SRTM3 objects."""
        global childFileListDownload
        global filelistDownloadActive
        mypid = os.getpid()
        if mypid in childFileListDownload and childFileListDownload[mypid].is_alive():
            if self.debug:
                print("still getting file list")
            return 0
        elif not os.path.isfile(self.filelist_file) and filelistDownloadActive == 0:
            self.createFileList()
            return 0
        elif not self.filelist:
            if self.debug:
                print("Filelist download complete, loading data ", self.filelist_file)
            data = open(self.filelist_file, 'rb')
            self.filelist = pickle.load(data)
            data.close()

        try:
            continent, filename = self.filelist[(int(lat), int(lon))]
        except KeyError:
            if len(self.filelist) > self.min_filelist_len:
                # we appear to have a full filelist - this must be ocean
                return SRTMOceanTile(int(lat), int(lon))
            return 0

        global childTileDownload
        mypid = os.getpid()
        if not os.path.exists(os.path.join(self.cachedir, filename)):
            if not mypid in childTileDownload or not childTileDownload[mypid].is_alive():
                try:
                    childTileDownload[mypid] = multiproc.Process(target=self.downloadTile, args=(str(continent), str(filename)))
                    childTileDownload[mypid].start()
                except Exception as ex:
                    if mypid in childTileDownload:
                        childTileDownload.pop(mypid)
                    return 0
                '''print("Getting Tile")'''
            return 0
        elif mypid in childTileDownload and childTileDownload[mypid].is_alive():
            '''print("Still Getting Tile")'''
            return 0
        # TODO: Currently we create a new tile object each time.
        # Caching is required for improved performance.
        try:
            return SRTMTile(os.path.join(self.cachedir, filename), int(lat), int(lon))
        except InvalidTileError:
            return 0

    def downloadTile(self, continent, filename):
        #Use HTTP
        mp_util.child_close_fds()
        if self.offline == 1:
            return
        filepath = "%s%s%s" % \
                     (self.directory,continent,filename)
        try:
            data = self.getURIWithRedirect(filepath)
            if data:
                self.ftpfile = open(os.path.join(self.cachedir, filename), 'wb')
                self.ftpfile.write(data)
                self.ftpfile.close()
                self.ftpfile = None
        except Exception as e:
            if not self.first_failure:
                print("SRTM Download failed %s on server %s" % (filepath, self.server))
                self.first_failure = True
            pass