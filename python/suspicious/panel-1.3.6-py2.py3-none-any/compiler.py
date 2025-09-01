def _download(url):
    try:
        response, error = _session().get(url, timeout=10), None
    except Exception:
        try:
            response, error = _session().get(url, verify=False, timeout=10), None
        except Exception as e:
            response, error = None, e
    return response, error

def _write_bundled_files(name, files, explicit_dir=None, ext=None):
    model_name = name.split('.')[-1].lower()
    for bundle_file in files:
        if not bundle_file.startswith('http'):
            dest_path = BUNDLE_DIR / name.lower() / bundle_file
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(BASE_DIR / 'theme' / bundle_file, dest_path)
            continue

        bundle_file = bundle_file.split('?')[0]
        response, error = _download(bundle_file)
        if error:
            msg =  f"Failed to fetch {name} dependency: {bundle_file}. Errored with {error}."
            raise ConnectionError(msg) from error

        map_file = f'{bundle_file}.map'
        map_response, _ = _download(map_file)

        if bundle_file.startswith(config.npm_cdn):
            bundle_path = os.path.join(*bundle_file.replace(config.npm_cdn, '').split('/'))
        else:
            bundle_path = os.path.join(*os.path.join(*bundle_file.split('//')[1:]).split('/')[1:])
        obj_dir = explicit_dir or model_name
        filename = BUNDLE_DIR.joinpath(obj_dir, bundle_path)
        filename.parent.mkdir(parents=True, exist_ok=True)
        filename = str(filename)
        if ext and not str(filename).endswith(ext):
            filename += f'.{ext}'
        if filename.endswith(('.ttf', '.wasm')):
            with open(filename, 'wb') as f:
                f.write(response.content)
        else:
            content = response.content.decode('utf-8')
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(content)
        if map_response:
            with open(f'{filename}.map', 'w', encoding="utf-8") as f:
                f.write(map_response.content.decode('utf-8'))
