def upload_data(
    dataset_identifier: str,
    files: Optional[List[Union[PathLike, LocalFile]]],
    files_to_exclude: Optional[List[PathLike]],
    fps: int,
    path: Optional[str],
    frames: bool,
    extract_views: bool = False,
    handle_as_slices: bool = False,
    preserve_folders: bool = False,
    verbose: bool = False,
    item_merge_mode: Optional[str] = None,
) -> None:
    """
    Uploads the provided files to the remote dataset.
    Exits the application if no dataset with the given name is found, the files in the given path
    have unsupported formats, or if there are no files found in the given Path.

    Parameters
    ----------
    dataset_identifier : str
        Slug of the dataset to retrieve.
    files : List[Union[PathLike, LocalFile]]
        List of files to upload. Can be None.
    files_to_exclude : List[PathLike]
        List of files to exclude from the file scan (which is done only if files is None).
    fps : int
        Frame rate to split videos in.
    path : Optional[str]
        If provided; files will be placed under this path in the v7 platform. If `preserve_folders`
        is `True` then it must be possible to draw a relative path from this folder to the one the
        files are in, otherwise an error will be raised.
    frames : bool
        Specify whether the files will be uploaded as a list of frames or not.
    extract_views : bool
        If providing a volume, specify whether to extract the orthogonal views or not.
    handle_as_slices : bool
        Whether to upload DICOM files as slices
    preserve_folders : bool
        Specify whether or not to preserve folder paths when uploading.
    verbose : bool
        Specify whether to have full traces print when uploading files or not.
    item_merge_mode : Optional[str]
        If set, each file path passed to `files_to_upload` behaves as follows:
        - Paths pointing directly to individual files are ignored
        - Paths pointing to folders of files will be uploaded according to the following mode rules.
          Note that folders will not be recursively searched, so only files in the first level of the folder will be uploaded:
            - "slots": Each file in the folder will be uploaded to a different slot of the same item.
            - "series": All `.dcm` files in the folder will be concatenated into a single slot. All other files are ignored.
            - "channels": Each file in the folder will be uploaded to a different channel of the same item.
    """
    client: Client = _load_client()
    try:
        max_workers: int = concurrent.futures.ThreadPoolExecutor()._max_workers  # type: ignore

        dataset: RemoteDataset = client.get_remote_dataset(
            dataset_identifier=dataset_identifier
        )

        sync_metadata: Progress = Progress(
            SpinnerColumn(), TextColumn("[bold blue]Syncing metadata")
        )

        overall_progress = Progress(
            TextColumn("[bold blue]{task.fields[filename]}"),
            BarColumn(),
            "{task.completed} of {task.total}",
        )

        file_progress = Progress(
            TextColumn("[bold green]{task.fields[filename]}", justify="right"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.1f}%",
            DownloadColumn(),
            "•",
            TransferSpeedColumn(),
            "•",
            TimeRemainingColumn(),
        )

        progress_table: Table = Table.grid()
        progress_table.add_row(sync_metadata)
        progress_table.add_row(file_progress)
        progress_table.add_row(overall_progress)
        with Live(progress_table):
            sync_task: TaskID = sync_metadata.add_task("")
            file_tasks: Dict[str, TaskID] = {}
            overall_task = overall_progress.add_task(
                "[green]Total progress",
                filename="Total progress",
                total=0,
                visible=False,
            )

            def progress_callback(
                total_file_count: NumberLike, file_advancement: NumberLike
            ) -> None:
                sync_metadata.update(sync_task, visible=False)
                overall_progress.update(
                    overall_task,
                    total=total_file_count,
                    advance=file_advancement,
                    visible=True,
                )

            def file_upload_callback(
                file_name: str,
                file_total_bytes: NumberLike,
                file_bytes_sent: NumberLike,
            ) -> None:
                if file_name not in file_tasks:
                    file_tasks[file_name] = file_progress.add_task(
                        f"[blue]{file_name}", filename=file_name, total=file_total_bytes
                    )

                # Rich has a concurrency issue, so sometimes updating progress
                # or removing a task fails. Wrapping this logic around a try/catch block
                # is a workaround, we should consider solving this properly (e.g.: using locks)
                try:
                    file_progress.update(
                        file_tasks[file_name], completed=file_bytes_sent
                    )

                    for task in file_progress.tasks:
                        if task.finished and len(file_progress.tasks) >= max_workers:
                            file_progress.remove_task(task.id)
                except Exception:
                    pass

            upload_manager = dataset.push(
                files,
                files_to_exclude=files_to_exclude,
                fps=fps,
                as_frames=frames,
                extract_views=extract_views,
                handle_as_slices=handle_as_slices,
                path=path,
                preserve_folders=preserve_folders,
                progress_callback=progress_callback,
                file_upload_callback=file_upload_callback,
                item_merge_mode=item_merge_mode,
            )
        console = Console(theme=_console_theme())

        console.print()

        if not upload_manager.blocked_count and not upload_manager.error_count:
            console.print(
                f"All {upload_manager.total_count} files have been successfully uploaded.\n",
                style="success",
            )
            return

        already_existing_items = []
        other_skipped_items = []
        for item in upload_manager.blocked_items:
            for slot in item.slots:
                if (slot.reason is not None) and (
                    slot.reason.upper() == BLOCKED_UPLOAD_ERROR_ALREADY_EXISTS
                ):
                    already_existing_items.append(item)
                else:
                    other_skipped_items.append(item)

        if already_existing_items:
            console.print(
                f"Skipped {len(already_existing_items)} files already in the dataset.\n",
                style="warning",
            )

        if upload_manager.error_count or other_skipped_items:
            error_count = upload_manager.error_count + len(other_skipped_items)
            console.print(
                f"{error_count} files couldn't be uploaded because an error occurred.\n",
                style="error",
            )

        if not verbose and upload_manager.error_count:
            console.print('Re-run with "--verbose" for further details')
            return

        error_table: Table = Table(
            "Dataset Item ID",
            "Filename",
            "Remote Path",
            "Stage",
            "Reason",
            show_header=True,
            header_style="bold cyan",
        )
        for item in upload_manager.blocked_items:
            for slot in item.slots:
                if (slot.reason is not None) and (
                    slot.reason.upper() != BLOCKED_UPLOAD_ERROR_ALREADY_EXISTS
                ):
                    error_table.add_row(
                        str(item.dataset_item_id),
                        item.filename,
                        item.path,
                        "UPLOAD_REQUEST",
                        slot.reason,
                    )
        for error in upload_manager.errors:
            for local_file in upload_manager.local_files:
                if local_file.local_path != error.file_path:
                    continue

                for pending_item in upload_manager.pending_items:
                    if pending_item.filename != local_file.data["filename"]:
                        continue

                    error_table.add_row(
                        str(pending_item.dataset_item_id),
                        pending_item.filename,
                        pending_item.path,
                        error.stage.name,
                        str(error.error),
                    )
                    break

        if error_table.row_count:
            console.print(error_table)
        print_new_version_info(client)
    except NotFound as e:
        _error(f"No dataset with name '{e.name}'")
    except UnsupportedFileType as e:
        _error(f"Unsupported file type {e.path.suffix} ({e.path.name})")
    except ValueError as e:
        _error(f"{e}")
