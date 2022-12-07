import pymysql,json

print('MySQL初始化')
mysqlname = input('mysql的用户：')
mysqlpasswd = input('mysql的密码：')
mysqlhost = input('mysql的host：')
mysqlport = input('mysql的端口：')

print('Token初始化')
tokenal = input('Token算法：')
tokenkey = input('Token密钥：')

print('Workdir初始化')
workdir = input('Workdir的地址：')

config = {
    "SQLURL": {
        "Login": f"mysql+pymysql://{mysqlname}:{mysqlpasswd}@{mysqlhost}:{mysqlport}/appagent"
    },
    "Token": {
        "KEY": f"{tokenkey}",
        "ALGORITHM": f"{tokenal}",
        "ACCESS_TOKEN_EXPIRE_MINUTE": 30
    },
    "Workdir": f"{workdir}"
}
with open('./Config.json','w') as f:
    json.dump(config,f,ensure_ascii = False,indent = 4)

mysqlname = 'root'
mysqlhost = 'localhost'
mysqlport = 3306
mysqlpasswd = 'qwert12345'
db = pymysql.connect(user = mysqlname,password = mysqlpasswd,host = mysqlhost,port = int(mysqlport),charset = 'utf8')
cursor = db.cursor()
createdatabase = 'create database if not exists appagent'
usedatabase = 'use appagent'
createtable = 'create table if not exists user (id int not null auto_increment,name varchar(20),password varchar(100),premission varchar(20),primary key(id))'
cursor.execute(createdatabase)
cursor.execute(usedatabase)
cursor.execute(createtable)
cursor.close()
db.close()





