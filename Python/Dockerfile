FROM kalilinux/kali-rolling
COPY / /appagent-server
WORKDIR /appagent-server
RUN apt update && apt install -y python3 python3-pip docker git
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install pyjwt fastapi[all] pymysql sqlalchemy gitpython cryptography docker-compose
EXPOSE 8080
CMD python3 Main.py