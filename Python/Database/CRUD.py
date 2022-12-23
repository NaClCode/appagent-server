import sqlalchemy
from Setting import SeeionLocal
from Models import User

db = SeeionLocal()
def get_user(name:str,password:str) -> object:
    return db.query(User).filter(User.name == name).filter(User.password == password).first()

def create_user(name:str,password:str,premisson:str) -> object:
    db_user = User(name = name,password = password,premission = premisson)
    if not db.query(User).filter(User.name == name).first():
        db.add(db_user)
        db.commit()
        return db_user
    else: return None
