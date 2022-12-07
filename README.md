# Appagent-Server

## 背景

运维绝大多数工作都是重复的Web应用部署和管理。
这些工作主要是拉取仓库、编写部署脚本、添加Nginx配置、添加域名解析，
部署脚本更是要与后端对接了解特定应用技术栈下的部署方法（如Java与C#之别）。
Token的前运维++h便提出使用Docker统一部署工作：后端在仓库中附带Dockerfile，
而运维只需要关心如何将Docker应用运行起来，不需要关心应用许多细节。
如此以来，部署工作便变得机械且重复，易于自动化。

## 功能

实现一个REST应用，实现应用部署和管理的自动化：

1. 鉴权（登录获取Token，调用接口需要持有Token）
2. 服务端应用管理：
   - 创建
   - 删除
   - 重启
   - 停止
   - 指定仓库
   - 修改配置（Nginx, Dockerfile, docker-compose）
   - 获取应用状态和日志
3. REST API

## 配置
- 必备软件：
  + Docker
  + MySQL
  + Git
- 必备模块：
  + fastapi[all]
  + pymysql
  + gitpython
  + sqlachemy
- 初始化：python3 Init.py
- 运行：python3 Main.py

## 下一步更新（1.0.1.0）
1. 自动添加域名解析
2. 硬盘容量监控和清理
3. 证书管理
4. 强化鉴权
5. 打包成docker应用
6. 修改一些特性