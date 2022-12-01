import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def log(ymlpath:str,container:str,user:dict):
    try:
        path = Path.getpath(user)
        os.chdir(f'{path}/{ymlpath}')
        return {'logs': os.system(f'docker-compose logs {container}'),
                'ps': os.system(f'docker-compose ps {container}'),
                'top': os.system(f'docker-compose top {container}')}
    except:
        raise HTTPException(status_code = 400,detail = 'Log Error')