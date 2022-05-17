import os
from dotenv import load_dotenv


load_dotenv()

class ConfigTelegram:
    work = '1' if bool(os.getenv('WORK', '')) else '0'
    token = os.getenv('TOKEN', '')
    admins = [
        int(os.getenv('ADMIN', 0)),
    ] if os.getenv('ADMIN', 0) else []

class ConfigFolder:
    folder = os.getcwd()
    folder_storage = os.path.join(
        folder,
        'storage'
    )
    file_use = os.path.join(
        folder_storage,
        'template.json'
    )
    value_template = {
        "users": ConfigTelegram.admins,
        "message":{
            1: "Максим всё ещё тянет лямку",
            0: "Максим всё ещё безработный",
        }
    }