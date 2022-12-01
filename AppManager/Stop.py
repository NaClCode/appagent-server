import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def stop(ymlpath:str,container:str,user:dict)->str:
    try:
        path = Path.getpath(user)
        os.chdir(f'{path}/{ymlpath}')
        os.system(f'docker-compose stop {container}')
        return 'Stop Succeed'
    except:
        raise HTTPException(status_code = 400,detail = 'Stop Error')