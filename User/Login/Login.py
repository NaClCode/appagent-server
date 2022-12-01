from fastapi import Form,Request,HTTPException
from fastapi import APIRouter
import os,sys,json
sys.path.append(f'{os.path.dirname(__file__)}'.replace('User/Login','Database'))
sys.path.append(f'{os.path.dirname(__file__)}')
import CRUD,Token

with open(f'{os.path.dirname(__file__)}'.replace('User/Login','Config.json')) as myjwt:
    myjwt = json.load(myjwt).get('Token')

applogin = APIRouter()

@applogin.api_route('/Login',methods = ('GET','POST'))
def token(req:Request,name = Form(None),password = Form(None)):
    try: user = CRUD.get_user(name,password)
    except: raise HTTPException(status_code = 400,detail = 'DataBase Error')
    if user:
        access_token_expires = Token.timedelta(minutes = myjwt.get('ACCESS_TOKEN_EXPIRE_MINUTE'))
        access_token = Token.create_access_token(data = {'name':name,'premission':user.premission},expires_delta = access_token_expires)
        return access_token
    else: raise HTTPException(status_code = 400,detail = 'Login Error')