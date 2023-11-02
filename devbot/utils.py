import yaml
import os
from pathlib import Path

# from https://github.com/itzlayz/teagram-tl
BASE_DIR = (
    "/data"
    if "DOCKER" in os.environ
    else os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
) 
BASE_PATH = Path(BASE_DIR)
PATH = f"{BASE_PATH}/devbot/"

def get_lang(locale: str) -> str:    # sourcery skip: merge-duplicate-blocks
    '''
    Function for get language flie
    
    :parametrs:

    locale: str
        string with lang code user

    :return: path to file with lang
    '''

    locale_path = f"{PATH}/locale"
    if locale == "ru":
        with open(f'{locale_path}/ru.yml', 'r') as f:
            data = yaml.safe_load(f)

    else:
        with open(f'{locale_path}/en.yml', 'r') as f:
            data = yaml.safe_load(f)

    return data


