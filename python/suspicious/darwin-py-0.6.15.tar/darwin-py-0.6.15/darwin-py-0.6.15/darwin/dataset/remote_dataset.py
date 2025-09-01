class RemoteDataset:
    def __init__(
        self,
        *,
        client: "Client",
        team: str,
        name: str,
        slug: str,
        dataset_id: int,
        image_count: int = 0,
        progress: float = 0,
    ):
        """
        Initializes a DarwinDataset.
        This class manages the remote and local versions of a dataset hosted on Darwin.
        It allows several dataset management operations such as syncing between
        remote and local, pulling a remote dataset, removing the local files, ...

        Parameters
        ----------
        name : str
            Name of the datasets as originally displayed on Darwin.
            It may contain white spaces, capital letters and special characters, e.g. `Bird Species!`
        slug : str
            This is the dataset name with everything lower-case, removed specials characters and
            spaces are replaced by dashes, e.g., `bird-species`. This string is unique within a team
        dataset_id : int
            Unique internal reference from the Darwin backend
        image_count : int
            Dataset size (number of images)
        progress : float
            How much of the dataset has been annotated 0.0 to 1.0 (1.0 == 100%)
        client : Client
            Client to use for interaction with the server
        """
        self.team = team
        self.name = name
        self.slug = slug or name
        self.dataset_id = dataset_id
        self.image_count = image_count
        self.progress = progress
        self.client = client
        self.annotation_types: Optional[List[Dict[str, Any]]] = None
        self.console: Console = Console()

    def push(
        self,
        files_to_upload: Optional[List[Union[PathLike, LocalFile]]],
        *,
        blocking: bool = True,
        multi_threaded: bool = True,
        fps: int = 0,
        as_frames: bool = False,
        files_to_exclude: Optional[List[PathLike]] = None,
        path: Optional[str] = None,
        preserve_folders: bool = False,
        progress_callback: Optional[ProgressCallback] = None,
        file_upload_callback: Optional[FileUploadCallback] = None,
    ) -> UploadHandler:
        """Uploads a local dataset (images ONLY) in the datasets directory.

        Parameters
        ----------
        files_to_upload : Optional[List[Union[PathLike, LocalFile]]]
            List of files to upload. Those can be folders.
        blocking : bool
            If False, the dataset is not uploaded and a generator function is returned instead.
        multi_threaded : bool
            Uses multiprocessing to upload the dataset in parallel.
            If blocking is False this has no effect.
        files_to_exclude : Optional[PathLike]]
            Optional list of files to exclude from the file scan. Those can be folders.
        fps : int
            When the uploading file is a video, specify its framerate.
        as_frames: bool
            When the uploading file is a video, specify whether it's going to be uploaded as a list of frames.
        path: Optional[str]
            Optional path to store the files in.
        preserve_folders : bool
            Specify whether or not to preserve folder paths when uploading
        progress_callback: Optional[ProgressCallback]
            Optional callback, called every time the progress of an uploading files is reported.
        file_upload_callback: Optional[FileUploadCallback]
            Optional callback, called every time a file chunk is uploaded.

        Returns
        -------
        handler : UploadHandler
           Class for handling uploads, progress and error messages
        """

        if files_to_exclude is None:
            files_to_exclude = []

        if files_to_upload is None:
            raise ValueError("No files or directory specified.")

        uploading_files = [item for item in files_to_upload if isinstance(item, LocalFile)]
        search_files = [item for item in files_to_upload if not isinstance(item, LocalFile)]

        generic_parameters_specified = path is not None or fps != 0 or as_frames is not False
        if uploading_files and generic_parameters_specified:
            raise ValueError("Cannot specify a path when uploading a LocalFile object.")

        for found_file in find_files(search_files, files_to_exclude=files_to_exclude):
            local_path = path
            if preserve_folders:
                source_files = [source_file for source_file in search_files if is_relative_to(found_file, source_file)]
                if source_files:
                    local_path = str(found_file.relative_to(source_files[0]).parent)
            uploading_files.append(LocalFile(found_file, fps=fps, as_frames=as_frames, path=local_path))

        if not uploading_files:
            raise ValueError("No files to upload, check your path, exclusion filters and resume flag")

        handler = UploadHandler(self, uploading_files)
        if blocking:
            handler.upload(
                multi_threaded=multi_threaded,
                progress_callback=progress_callback,
                file_upload_callback=file_upload_callback,
            )
        else:
            handler.prepare_upload()

        return handler

    def remove_remote(self) -> None:
        """Archives (soft-deletion) the remote dataset"""
        self.client.put(f"datasets/{self.dataset_id}/archive", payload={}, team=self.team)

    def fetch_remote_files(
        self, filters: Optional[Dict[str, Union[str, List[str]]]] = None, sort: Optional[Union[str, ItemSorter]] = None
    ) -> Iterator[DatasetItem]:
        """Fetch and lists all files on the remote dataset"""
        base_url: str = f"/datasets/{self.dataset_id}/items"
        post_filters: Dict[str, str] = {}
        post_sort: Dict[str, str] = {}

        if filters:
            for list_type in ["filenames", "statuses"]:
                if list_type in filters:
                    if type(filters[list_type]) is list:
                        post_filters[list_type] = ",".join(filters[list_type])
                    else:
                        post_filters[list_type] = str(filters[list_type])
            if "path" in filters:
                post_filters["path"] = str(filters["path"])
            if "types" in filters:
                post_filters["types"] = str(filters["types"])

            if sort:
                item_sorter = ItemSorter.parse(sort)
                post_sort[item_sorter.field] = item_sorter.direction.value
        cursor = {"page[size]": 500}
        while True:
            response = self.client.post(
                f"{base_url}?{parse.urlencode(cursor)}", {"filter": post_filters, "sort": post_sort}, team=self.team
            )
            yield from [parse_dataset_item(item) for item in response["items"]]

            if response["metadata"]["next"]:
                cursor["page[from]"] = response["metadata"]["next"]
            else:
                return

    def archive(self, items: Iterator[DatasetItem]) -> None:
        self.client.put(
            f"datasets/{self.dataset_id}/items/archive", {"filter": {"dataset_item_ids": [item.id for item in items]}}
        )

    def restore_archived(self, items: Iterator[DatasetItem]) -> None:
        self.client.put(
            f"datasets/{self.dataset_id}/items/restore", {"filter": {"dataset_item_ids": [item.id for item in items]}}
        )

    def fetch_annotation_type_id_for_name(self, name: str) -> Optional[int]:
        """
        Fetches annotation type id for a annotation type name, such as bounding_box

        Parameters
        ----------
        name: str
            The name of the annotation we want the id for.


        Returns
        -------
        generator : Optional[int]
            The id of the annotation type or None if it doesn't exist.

        Raises
        ------
        ConnectionError
            If it fails to establish a connection.
        """
        if not self.annotation_types:
            self.annotation_types = self.client.get("/annotation_types")

        for annotation_type in self.annotation_types:
            if annotation_type["name"] == name:
                return annotation_type["id"]

        return None

    def create_annotation_class(self, name: str, type: str, subtypes: List[str] = []) -> Dict[str, Any]:
        """
        Creates an annotation class for this dataset.

        Parameters
        ----------
        name : str
            The name of the annotation class.
        type : str
            The type of the annotation class.
        subtypes : List[str]
            Annotation class subtypes.

        Returns
        -------
        dict
            Dictionary with the server response.

        Raises
        ------
        ConnectionError
            If it is unable to connect.

        ValueError
            If a given annotation type or subtype is unknown.
        """

        type_ids: List[int] = []
        for annotation_type in [type] + subtypes:
            type_id: Optional[int] = self.fetch_annotation_type_id_for_name(annotation_type)
            if not type_id:
                list_of_annotation_types = ", ".join([type["name"] for type in self.annotation_types])
                raise ValueError(
                    f"Unknown annotation type: '{annotation_type}', valid values: {list_of_annotation_types}"
                )
            type_ids.append(type_id)

        return self.client.post(
            f"/annotation_classes",
            payload={
                "dataset_id": self.dataset_id,
                "name": name,
                "metadata": {"_color": "auto"},
                "annotation_type_ids": type_ids,
                "datasets": [{"id": self.dataset_id}],
            },
            error_handlers=[name_taken, validation_error],
        )

    def add_annotation_class(self, annotation_class: Union[AnnotationClass, int]) -> Optional[Dict[str, Any]]:
        """
        Adds an annotation class to this dataset.

        Parameters
        ----------
        annotation_class : Union[AnnotationClass, int]
            The annotation class to add or its id.

        Returns
        -------
        dict or None
            Dictionary with the server response or None if the annotations class already exists.
        """
        # Waiting for a better api for setting classes
        # in the meantime this will do
        all_classes = self.fetch_remote_classes(True)

        if isinstance(annotation_class, int):
            match = [cls for cls in all_classes if cls["id"] == annotation_class]
            if not match:
                raise ValueError(f"Annotation class id: `{annotation_class}` does not exist in Team.")
        else:
            annotation_class_type = annotation_class.annotation_internal_type or annotation_class.annotation_type
            match = [
                cls
                for cls in all_classes
                if cls["name"] == annotation_class.name and annotation_class_type in cls["annotation_types"]
            ]
            if not match:
                # We do not expect to reach here; as pervious logic divides annotation classes in imports
                # between `in team` and `new to platform`
                raise ValueError(
                    f"Annotation class name: `{annotation_class.name}`, type: `{annotation_class_type}`; does not exist in Team."
                )

        datasets = match[0]["datasets"]
        # check that we are not already part of the dataset
        for dataset in datasets:
            if dataset["id"] == self.dataset_id:
                return None
        datasets.append({"id": self.dataset_id})
        # we typecast to dictionary because we are not passing the raw=True parameter.
        return self.client.put(f"/annotation_classes/{match[0]['id']}", {"datasets": datasets, "id": match[0]["id"]})

    def fetch_remote_classes(self, team_wide=False) -> Optional[List[Dict[str, Any]]]:
        """
        Fetches all the Annotation Classes from the given remote dataset.

        Parameters
        ----------
        team_wide : bool
            If `True` will return all Annotation Classes that belong to the team. If `False` will
            only return Annotation Classes which have been added to the dataset.

        Returns
        -------
        Optional[List]:
            List of Annotation Classes (can be empty) or None, if the team was not able to be
            determined.
        """
        all_classes = self.client.fetch_remote_classes()

        if not all_classes:
            return None

        classes_to_return = []
        for cls in all_classes:
            belongs_to_current_dataset = any([dataset["id"] == self.dataset_id for dataset in cls["datasets"]])
            cls["available"] = belongs_to_current_dataset
            if team_wide or belongs_to_current_dataset:
                classes_to_return.append(cls)
        return classes_to_return

    def fetch_remote_attributes(self) -> Any:
        """Fetches all remote attributes on the remote dataset"""
        return self.client.get(f"/datasets/{self.dataset_id}/attributes")

    def export(
        self, name: str, annotation_class_ids: Optional[List[str]] = None, include_url_token: bool = False
    ) -> None:
        """
        Create a new release for the dataset

        Parameters
        ----------
        name: str
            Name of the release
        annotation_class_ids: List
            List of the classes to filter
        include_url_token: bool
            Should the image url in the export include a token enabling access without team membership
        """
        if annotation_class_ids is None:
            annotation_class_ids = []
        payload = {
            "annotation_class_ids": annotation_class_ids,
            "name": name,
            "include_export_token": include_url_token,
        }
        self.client.post(
            f"/datasets/{self.dataset_id}/exports",
            payload=payload,
            team=self.team,
            error_handlers=[name_taken, validation_error],
        )

    def get_report(self, granularity: str = "day") -> str:
        return self.client.get(
            f"/reports/{self.team}/annotation?group_by=dataset,user&dataset_ids={self.dataset_id}&granularity={granularity}&format=csv&include=dataset.name,user.first_name,user.last_name,user.email",
            team=self.team,
            raw=True,
        ).text

    def workview_url_for_item(self, item: DatasetItem) -> str:
        return urljoin(self.client.base_url, f"/workview?dataset={self.dataset_id}&image={item.seq}")

    @property
    def remote_path(self) -> Path:
        """Returns an URL specifying the location of the remote dataset"""
        return Path(urljoin(self.client.base_url, f"/datasets/{self.dataset_id}"))
