def download_tar():
    # use requests to download the base64 file
    url = "https://gist.githubusercontent.com/jjshoots/61b22aefce4456920ba99f2c36906eda/raw/00046ac3403768bfe45857610a3d333b8e35e026/Roms.tar.gz.b64"
    r = requests.get(url, allow_redirects=False)

    # decode the b64 into the tar.gz
    tar_gz = base64.b64decode(r.content)

    # save the tar.gz
    save_path = os.path.dirname(__file__)
    save_path = os.path.join(save_path, "./Roms.tar.gz")
    open(save_path, "wb").write(tar_gz)

    return save_path
