import git,os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

def create(gitname:str,gitpassword:str,remotepath:str,user:dir)->str:
    path = Path.getpath(user)
    os.system(f'rm -rf {path}')
    os.system(f'mkdir {path}')
    repo = git.Repo.init()
    remoteurl = remotepath.replace('https://',f'https://{gitname}:{gitpassword}@')
    try: repo.clone_from(url = remoteurl,to_path = path)
    except: raise HTTPException(status_code = 400,detail = 'Git Error')
    '''
    try:
        os.system(f'docker-compose -f {path}/{ymlpath} up -d')
        return 'Create Succeed'
    except: 
        raise HTTPException(status_code = 400,detail = os.system(f'docker-compose -f {path}/{ymlpath} config -q'))
    '''