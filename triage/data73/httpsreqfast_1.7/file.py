import shutil


def copy_file(src_path : str, destination_path : str):
    try:
        return shutil.copy2(src_path, destination_path)
    except:
        pass
