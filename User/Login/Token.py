from fastapi import HTTPException
from datetime import datetime,timedelta
import json,os,jwt
from pydantic import BaseModel

with open(f'{os.path.dirname(__file__)}'.replace('User/Login','Config.json')) as myjwt:
    myjwt = json.load(myjwt).get('Token')

class Token(BaseModel):
    access_token: str
    token_type:str

def create_access_token(data:dict,expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp':expire})
    jwt_encoded = jwt.encode(to_encode,myjwt.get('KEY'),myjwt.get('ALGORITHM'))
    return jwt_encoded

def get_access_token(token)->dict:
    try:
        token = jwt.decode(token,myjwt.get('KEY'),myjwt.get('ALGORITHM'))
        return token
    except:
        raise HTTPException(status_code = 405,detail = 'Token Error')