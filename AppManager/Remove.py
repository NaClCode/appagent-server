import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def remove(ymlpath:str,container:str,user:dict)->str:
    try:
        path = Path.getpath(user)
        os.chdir(f'{path}/{ymlpath}')
        if container == None: os.system(f'docker-compose rm -sv {container}')
        else: os.system(f'docker-compose rm -s')
        return 'Remove Succeed'
    except:
        raise HTTPException(status_code = 400,detail = 'Remove Error')
