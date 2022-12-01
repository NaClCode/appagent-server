import os,git,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def pull(gitname:str,gitpassword:str,gitpath:str,pullurl:str,user:dict)->str:
    try:
        path = Path.getpath(user)
        os.chdir(f'{path}')
        repo = git.Repo(f'{path}/{gitpath}')
        repo = repo.remote()
        pullurl = pullurl.replace('https://',f'https://{gitname}:{gitpassword}@')
        repo.pull(pullurl)
        return 'Pull Succeed'
    except:
        raise HTTPException(status_code = 400,detail = 'Pull Error')
