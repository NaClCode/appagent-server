import os,sys,subprocess
from fastapi import HTTPException
sys.path.append(os.path.dirname(__file__))
import Path

class File:
    def __init__(self,listpath:str,user:dict):
        self.listpath = listpath
        self.user = user
    def tree(self):
        try:
            os.chdir(f'{Path.getpath(self.user)}/{self.listpath}')
            return subprocess.Popen(['tree'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
        except:
            raise HTTPException(status_code = 400,detail = 'Tree Error')
    def dfh(self):
        try:
            os.chdir(f'{Path.getpath(self.user)}/{self.listpath}')
            return subprocess.Popen(['du','-h'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
        except:
            raise HTTPException(status_code = 400,detail = 'Df-h Error')
    def rm(self):
        try:
            return subprocess.Popen(['rm','-rf',f'{Path.getpath(self.user)}/{self.listpath}'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
        except:
            raise HTTPException(status_code = 400,detail = 'Remove Error')