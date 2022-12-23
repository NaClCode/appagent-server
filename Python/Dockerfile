FROM python
COPY / /appagent-server
WORKDIR /appagent-server
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install fastapi[all] pyjwt pymysql sqlalchemy gitpython cryptography
RUN git config --global user.name NaCl
RUN git config --global user.email nacl@whut.edu.com
EXPOSE 8080
CMD python3 Main.py