from fastapi import FastAPI
from AppManager.Main import appmanager
from User.Main import appuser
import uvicorn

app = FastAPI()
app.include_router(appuser,prefix = '/User')
app.include_router(appmanager,prefix = '/Main')

if __name__ == '__main__':
    uvicorn.run(app)