from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql,json,os

with open(f'{os.path.dirname(__file__)}'.replace('Database','Config.json')) as sql:
    sql = json.load(sql)

engine = create_engine(sql.get('SQLURL').get('Login'),echo = False)
SeeionLocal = sessionmaker(autocommit = False,autoflush = False,bind = engine)
Base = declarative_base()