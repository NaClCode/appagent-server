from fastapi import APIRouter
from fastapi import Header,Form,Request,UploadFile,File
import os,sys
sys.path.append(f'{os.path.dirname(__file__)}'.replace('AppManager','User'))
sys.path.append(os.path.dirname(__file__))
import Token,Git,Files,Docker

appmanager = APIRouter()

@appmanager.post('/Git/{CMD}')
def create(req:Request,CMD,gitname = Form(None),gitpassword = Form(None),giturl = Form(None),dest = Form(None),branch = Form(None),token = Header(None)):
    git = Git.Git(gitname,gitpassword,giturl,dest,branch,Token.get_access_token(token))
    if CMD == 'Clone': return git.clone()
    elif CMD == 'Pull': return git.pull()
    else: return 'Error'

@appmanager.post('/Docker/{CMD}')
def app(req:Request,CMD,ymlpath = Form(None),container = Form(None),token = Header(None)):
    docker = Docker.Docker(ymlpath,container,Token.get_access_token(token))
    if CMD == 'Restart': return docker.restart()
    elif CMD == 'Up': return docker.up()
    elif CMD == 'Stop': return docker.stop()
    elif CMD == 'Log': return docker.log()
    elif CMD == 'Remove': return docker.remove()
    elif CMD == 'Start' : return docker.start()
    elif CMD == 'Down' : return docker.down()
    else: return 'Error'

@appmanager.put('/Modify')
async def modify(req:Request,ymlpath = Form(None),container = Form(None),destpath = Form(None),modifyfile:UploadFile = File(None),token = Header(None)):
    content = await modifyfile.read()
    docker = Docker.Docker(ymlpath,container,Token.get_access_token(token))
    return docker.modify(destpath,content)
    pass

@appmanager.post('/File/{CMD}')
def file(req:Request,CMD,listpath = Form(None),token = Header(None)):
    file = Files.File(listpath,Token.get_access_token(token))
    if CMD == 'Tree': return file.tree()
    elif CMD == 'Df-h': return file.dfh()
    elif CMD == 'Rm': return file.rm()
    else: return 'Error'