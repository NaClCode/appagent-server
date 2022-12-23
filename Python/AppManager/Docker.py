import os,sys
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

class Docker:
    def __init__(self,ymlpath:str,container:str,user:dict):
        self.__container = container
        self.__path = Path.getpath(user) 
        os.chdir(f'{self.__path}{ymlpath}')

    def log(self)->dict:
        try:  return {'logs': os.system(f'docker-compose logs {self.__container}'),
                    'ps': os.system(f'docker-compose ps {self.__container}'),
                    'top': os.system(f'docker-compose top {self.__container}')}
        except: raise HTTPException(status_code = 400,detail = 'Log Error')

    def remove(self)->str:
        try:
            os.system(f'docker-compose rm -sv {self.__container}')
            return 'Remove Succeed'
        except: raise HTTPException(status_code = 400,detail = 'Remove Error')

    def up(self)->str:
         try:
            os.system(f'docker-compose up -d')
            return 'Up Succeed'
         except: raise HTTPException(status_code = 400,detail = 'Up Error')

    def restart(self):
        try:
            os.system(f'docker-compose restart {self.__container}')
            return 'Restart Succeed'
        except: raise HTTPException(status_code = 400,detail = 'Restart Error')

    def stop(self)->str:
        try:
            os.system(f'docker-compose stop {self.__container}')
            return 'Stop Succeed'
        except:
            raise HTTPException(status_code = 400,detail = 'Stop Error')

    def down(self)->str:
        try:
            os.system(f'docker-compose down')
            return 'Down Succeed'
        except:
            raise HTTPException(status_code = 400,detail = 'Down Error')

    def start(self)->str:
        try:
            os.system(f'docker-compose start {self.__container}')
            return 'Start Succeed'
        except:
            raise HTTPException(status_code = 400,detail = 'Start Error')

    def modify(self,content,destpath:str)->str:
        try:
            with open(f'{self.__path}/{destpath}','wb') as f:
                f.write(content)
            self.restart()
            return 'Modify Succeed'
        except:
            raise HTTPException(status_code = 400,detail = 'Modify Error')

