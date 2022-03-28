from os.path import curdir, abspath, exists
from pathlib import Path
from shutil import rmtree


def cleanup():
    data_folder = Path(abspath(curdir))
    temp_folder = data_folder / "temp"

    if exists(temp_folder) and temp_folder.is_dir():
        rmtree(temp_folder)
