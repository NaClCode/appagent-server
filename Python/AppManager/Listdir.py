import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def listdir(listpath:str,user:dict):
    try:
        path = Path.getpath(user)
        os.chdir(f'{path}/{listpath}')
        return os.listdir()
    except:
        raise HTTPException(status_code = 400,detail = 'Listdir Error')