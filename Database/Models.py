from sqlalchemy import Column,Integer,VARCHAR
from Setting import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True,autoincrement = True)
    name = Column(VARCHAR(20),default = None, nullable = False,comment = 'name')
    password = Column(VARCHAR(100),default = None, nullable = False,comment = 'password')
    premission = Column(VARCHAR(20),default = None, nullable = False,comment = 'premission')
    def __repr__(self):
        return f'User : name : {self.name} , premission : {self.premission}'