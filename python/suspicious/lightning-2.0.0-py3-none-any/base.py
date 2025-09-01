def _download_command(
    command_name: str,
    cls_path: str,
    cls_name: str,
    app_id: Optional[str] = None,
    debug_mode: bool = False,
    target_file: Optional[str] = None,
) -> ClientCommand:
    # TODO: This is a skateboard implementation and the final version will rely on versioned
    # immutable commands for security concerns
    command_name = command_name.replace(" ", "_")
    tmpdir = None
    if not target_file:
        tmpdir = osp.join(gettempdir(), f"{getuser()}_commands")
        makedirs(tmpdir)
        target_file = osp.join(tmpdir, f"{command_name}.py")

    if not debug_mode:
        if app_id:
            if not os.path.exists(target_file):
                client = LightningClient(retry=False)
                project_id = _get_project(client).project_id
                response = client.lightningapp_instance_service_list_lightningapp_instance_artifacts(
                    project_id=project_id, id=app_id
                )
                for artifact in response.artifacts:
                    if f"commands/{command_name}.py" == artifact.filename:
                        resp = requests.get(artifact.url, allow_redirects=True)

                        with open(target_file, "wb") as f:
                            f.write(resp.content)
        else:
            shutil.copy(cls_path, target_file)

    spec = spec_from_file_location(cls_name, target_file)
    mod = module_from_spec(spec)
    sys.modules[cls_name] = mod
    spec.loader.exec_module(mod)
    command_type = getattr(mod, cls_name)
    if issubclass(command_type, ClientCommand):
        command = command_type(method=None)
    else:
        raise ValueError(f"Expected class {cls_name} for command {command_name} to be a `ClientCommand`.")
    if tmpdir and os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)
    return command