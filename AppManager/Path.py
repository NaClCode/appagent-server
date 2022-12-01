import json,os

def getpath(user:dict)->str:
    with open(f'{os.path.dirname(__file__)}'.replace('AppManager','Config.json')) as workdir:
        workdir = json.load(workdir).get("Workdir")
    path = f'{workdir}/{user.get("name")}'
    return path