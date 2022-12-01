from fastapi import Header,Body,Form,Request,HTTPException
from fastapi import APIRouter
import os,sys
sys.path.append(f'{os.path.dirname(__file__)}'.replace('User/Register','Database'))
import CRUD

appregister = APIRouter()

@appregister.api_route('/Register',methods = ('GET','POST'))
def token(req:Request,name = Form(None),password = Form(None)):
    #try: 
    user = CRUD.create_user(name,password,'normal')
    #except: raise HTTPException(status_code = 400,detail = 'DataBase Error')
    if user:
        return 'Succeed'
    else: 
        raise HTTPException(status_code = 400,detail = 'Register Error')