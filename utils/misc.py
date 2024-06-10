import os
import shutil

def create_dir(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def remove_dir(dir_path: str) -> None:
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

def remove_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)

def get_subdirs(dir_path: str) -> list[str]:
    return [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]