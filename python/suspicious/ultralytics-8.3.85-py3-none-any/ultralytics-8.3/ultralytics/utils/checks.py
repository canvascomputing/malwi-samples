def check_imgsz(imgsz, stride=32, min_dim=1, max_dim=2, floor=0):
    """
    Verify image size is a multiple of the given stride in each dimension. If the image size is not a multiple of the
    stride, update it to the nearest multiple of the stride that is greater than or equal to the given floor value.

    Args:
        imgsz (int | cList[int]): Image size.
        stride (int): Stride value.
        min_dim (int): Minimum number of dimensions.
        max_dim (int): Maximum number of dimensions.
        floor (int): Minimum allowed value for image size.

    Returns:
        (List[int] | int): Updated image size.
    """
    # Convert stride to integer if it is a tensor
    stride = int(stride.max() if isinstance(stride, torch.Tensor) else stride)

    # Convert image size to list if it is an integer
    if isinstance(imgsz, int):
        imgsz = [imgsz]
    elif isinstance(imgsz, (list, tuple)):
        imgsz = list(imgsz)
    elif isinstance(imgsz, str):  # i.e. '640' or '[640,640]'
        imgsz = [int(imgsz)] if imgsz.isnumeric() else eval(imgsz)
    else:
        raise TypeError(
            f"'imgsz={imgsz}' is of invalid type {type(imgsz).__name__}. "
            f"Valid imgsz types are int i.e. 'imgsz=640' or list i.e. 'imgsz=[640,640]'"
        )

    # Apply max_dim
    if len(imgsz) > max_dim:
        msg = (
            "'train' and 'val' imgsz must be an integer, while 'predict' and 'export' imgsz may be a [h, w] list "
            "or an integer, i.e. 'yolo export imgsz=640,480' or 'yolo export imgsz=640'"
        )
        if max_dim != 1:
            raise ValueError(f"imgsz={imgsz} is not a valid image size. {msg}")
        LOGGER.warning(f"WARNING ⚠️ updating to 'imgsz={max(imgsz)}'. {msg}")
        imgsz = [max(imgsz)]
    # Make image size a multiple of the stride
    sz = [max(math.ceil(x / stride) * stride, floor) for x in imgsz]

    # Print warning message if image size was updated
    if sz != imgsz:
        LOGGER.warning(f"WARNING ⚠️ imgsz={imgsz} must be multiple of max stride {stride}, updating to {sz}")

    # Add missing dimensions if necessary
    sz = [sz[0], sz[0]] if min_dim == 2 and len(sz) == 1 else sz[0] if min_dim == 1 and len(sz) == 1 else sz

    return sz


def check_latest_pypi_version(package_name="ultralytics"):
    """
    Returns the latest version of a PyPI package without downloading or installing it.

    Args:
        package_name (str): The name of the package to find the latest version for.

    Returns:
        (str): The latest version of the package.
    """
    try:
        requests.packages.urllib3.disable_warnings()  # Disable the InsecureRequestWarning
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=3)
        if response.status_code == 200:
            return response.json()["info"]["version"]
    except Exception:
        return None


@ThreadingLocked()
def check_font(font="Arial.ttf"):
    """
    Find font locally or download to user's configuration directory if it does not already exist.

    Args:
        font (str): Path or name of font.

    Returns:
        file (Path): Resolved font file path.
    """
    from matplotlib import font_manager

    # Check USER_CONFIG_DIR
    name = Path(font).name
    file = USER_CONFIG_DIR / name
    if file.exists():
        return file

    # Check system fonts
    matches = [s for s in font_manager.findSystemFonts() if font in s]
    if any(matches):
        return matches[0]

    # Download to USER_CONFIG_DIR if missing
    url = f"https://github.com/ultralytics/assets/releases/download/v0.0.0/{name}"
    if downloads.is_url(url, check=True):
        downloads.safe_download(url=url, file=file)
        return file


def check_file(file, suffix="", download=True, download_dir=".", hard=True):
    """Search/download file (if necessary) and return path."""
    check_suffix(file, suffix)  # optional
    file = str(file).strip()  # convert to string and strip spaces
    file = check_yolov5u_filename(file)  # yolov5n -> yolov5nu
    if (
        not file
        or ("://" not in file and Path(file).exists())  # '://' check required in Windows Python<3.10
        or file.lower().startswith("grpc://")
    ):  # file exists or gRPC Triton images
        return file
    elif download and file.lower().startswith(("https://", "http://", "rtsp://", "rtmp://", "tcp://")):  # download
        url = file  # warning: Pathlib turns :// -> :/
        file = Path(download_dir) / url2file(file)  # '%2F' to '/', split https://url.com/file.txt?auth
        if file.exists():
            LOGGER.info(f"Found {clean_url(url)} locally at {file}")  # file already exists
        else:
            downloads.safe_download(url=url, file=file, unzip=False)
        return str(file)
    else:  # search
        files = glob.glob(str(ROOT / "**" / file), recursive=True) or glob.glob(str(ROOT.parent / file))  # find file
        if not files and hard:
            raise FileNotFoundError(f"'{file}' does not exist")
        elif len(files) > 1 and hard:
            raise FileNotFoundError(f"Multiple files match '{file}', specify exact path: {files}")
        return files[0] if len(files) else []  # return file


def is_sudo_available() -> bool:
    """
    Check if the sudo command is available in the environment.

    Returns:
        (bool): True if the sudo command is available, False otherwise.
    """
    if WINDOWS:
        return False
    cmd = "sudo --version"
    return subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
