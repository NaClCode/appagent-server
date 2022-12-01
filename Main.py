from fastapi import FastAPI,Depends
from User.Login.Login import applogin,Token
from AppManager.Main import appmanager
from User.Register.Register import appregister
import uvicorn

app = FastAPI()
app.include_router(applogin,prefix = '')
app.include_router(appmanager,prefix = '/Main')
app.include_router(appregister,prefix = '')

if __name__ == '__main__':
    uvicorn.run(app)