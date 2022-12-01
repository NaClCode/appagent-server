import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def restart(ymlpath:str,container:str,user:dict):
    try:
        path = Path.getpath(user)
        os.chdir(f'{path}/{ymlpath}')
        os.system(f'docker-compose restart {container}')
        return 'Restart Succeed'
    except:
        raise HTTPException(status_code = 400,detail = 'Restart Error')
