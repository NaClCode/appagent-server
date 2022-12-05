import git,os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

class Git:
    def __init__(self,gitname:str,gitpassword:str,giturl:str,dest:str,branch:str,user:dict):
        self.__giturl = giturl.replace('https://',f'https://{gitname}:{gitpassword}@')
        self.__path = f'{Path.getpath(user)}{dest}'
        self.__branch = branch
        os.system(f'mkdir {self.__path}')

    def clone(self):
        os.system(f'rm -rf {self.__path} && mkdir {self.__path}')
        repo = git.Repo().init()
        repo.clone_from(url = self.__giturl,to_path = self.__path,branch = self.__branch)
        #except: raise HTTPException(status_code = 400,detail = 'Clone Error')

    def pull(self)->str:
        try:
            os.chdir(self.__path)
            repo = git.Repo()
            repo = repo.remote().pull(branch = self.__branch)
            return 'Pull Succeed'
        except:
            raise HTTPException(status_code = 400,detail = 'Pull Error')