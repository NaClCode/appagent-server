import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def modifyyml(content,destpath:str,user:dict)->str:
    try:
        path = Path.getpath(user)
        with open(f'{path}/{destpath}','wb') as f:
            f.write(content)
        return 'Modifyyml Succeed'
    except:
        raise HTTPException(status_code = 400,detail = 'Modifyyml Error')

def modifynignx(content,destpath:str,user:dict)->str:
    try:
        path = Path.getpath(user)
        with open(f'{path}/{destpath}','wb') as f:
            f.write(content)
        return 'Modifynignx Succeed'
    except:
        raise HTTPException(status_code = 400,detail = 'Modifynignx Error')
 