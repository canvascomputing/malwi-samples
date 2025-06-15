import shutil


def copy_file(src_path : str, destination_path : str):
    return shutil.copy2(src_path, destination_path)
