import os
from venv import logger
from box import Box
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
import json
from logging import Logger
from ensure import ensure_annotations
from typing import Any
from pathlib import Path
import joblib

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open (path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully ")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def create_directories(path_to_directories :list, verbose=True):
    for directory in path_to_directories:
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logger.info(f"Creating Directory {directory}")

@ensure_annotations
def read_json(path:Path,data:dict) -> dict:
   with open(Path,"w") as f:
       json.dump(data,f,indent=4)

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"Json file loaded succesfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data, filename=path)
    logger.inf0(f"Binary file saved at : {path}")

def load_bin(path:Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded succesfully from : {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"