from fastapi import APIRouter
from fastapi import Header,Form,Request,UploadFile,File
import os,sys
sys.path.append(f'{os.path.dirname(__file__)}'.replace('AppManager','User/Login'))
sys.path.append(os.path.dirname(__file__))
import Token,Create,Remove,Restart,Stop,Log,Modify,Pull,Listdir

appmanager = APIRouter()

@appmanager.post('/Create')
def create(req:Request,gitname = Form(None),gitpassword = Form(None),remotepath = Form(None),token = Header(None)):
    return {'Create':Create.create(gitname,gitpassword,remotepath,Token.get_access_token(token))}

@appmanager.delete('/Remove')
def remove(req:Request,ymlpath = Form(None),container = Form(None),token = Header(None)):
    return {'Remove':Remove.remove(ymlpath,container,Token.get_access_token(token))}

@appmanager.post('/Restart')
def restart(req:Request,ymlpath = Form(None),container = Form(None),token = Header(None)):
    return {'Restart':Restart.restart(ymlpath,container,Token.get_access_token(token))}

@appmanager.post('/Stop')
def restart(req:Request,ymlpath = Form(None),container = Form(None),token = Header(None)):
    return {'Stop':Stop.stop(ymlpath,container,Token.get_access_token(token))}

@appmanager.post('/Logs')
def logs(req:Request,ymlpath = Form(None),container = Form(None),token = Header(None)):
    return {'Logs':Log.log(ymlpath,container,Token.get_access_token(token))}

@appmanager.put('/Modifyyml')
async def modifyyml(req:Request,destpath = Form(None),modifyfile:UploadFile = File(None),token = Header(None)):
    content = await modifyfile.read()
    return {'Modifyyml':Modify.modifyyml(content,destpath,Token.get_access_token(token))}

@appmanager.put('/Modifynignx')
async def modifynignx(req:Request,destpath = Form(None),modifyfile:UploadFile = File(None),token = Header(None)):
    content = await modifyfile.read()
    return {'Modifynignx':Modify.modifynignx(content,destpath,Token.get_access_token(token))}

@appmanager.post('/Pull')
def commit(req:Request,pullurl = Form(None),token = Header(None)):
    return {'Pull':Pull.pull(pullurl,Token.get_access_token(token))}

@appmanager.post('/Listdir')
def commit(req:Request,listpath = Form(None),token = Header(None)):
    return {'Listdir':Listdir.listdir(listpath,Token.get_access_token(token))}
