import os
import json
from config import (
    ConfigFolder, 
    ConfigTelegram
)


def check_folder(path_folder:str) -> None:
    return (
            os.path.exists(path_folder) and os.path.isdir(path_folder)
        ) or os.mkdir(path_folder)

def check_empty_values() -> bool:
    with open(ConfigFolder.file_use, 'r') as file_new:
        file_read = json.load(file_new)
    return file_read.get('message', {}).get(True, '') and file_read.get('message', {}).get(False, '')

def write_json(file_write:dict=ConfigFolder.value_template) -> None:
    with open(ConfigFolder.file_use, 'w') as file_new:
        json.dump(
            file_write,
            file_new, 
            sort_keys = False,
            indent=4
        )

def develop_file_string() -> set:
    """
    Function which is dedicated to develop the values
    """
    check_folder(ConfigFolder.folder_storage)
    if not (
        os.path.exists(ConfigFolder.file_use) and 
        os.path.isfile(ConfigFolder.file_use)
    ):
        write_json()    
    if not check_empty_values():
        with open(ConfigFolder.file_use, 'r') as file_new:
            file_read = json.load(file_new)
        write_json(
            {
                "users": file_read.get("users", []),
                "message": ConfigFolder.value_template.get("message", {})
            }
        )
    with open(ConfigFolder.file_use, 'r') as file_new:
        file_read = json.load(file_new)
    return file_read.get('users', []), \
        file_read.get('message', {}).get(ConfigTelegram.work, '')