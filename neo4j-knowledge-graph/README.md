# 图数据库

Neo4j 4.4.30

## Neo4j安装

可根据[官网](https://neo4j.com/)指导安装数据库
Neo4j数据库操作请查看[官方文档](https://neo4j.com/docs/)

## 数据库导入


### 1 加载kclass.db.dump
```bash
./bin/neo4j-admin.bat load --from=/data/kclass.db.dump --database=kclass.db --force 
```
### 2 Neo4j安装路径下 修改配置文件 **/conf/neo4j.conf**
```python
# The name of the database to mount
dbms.defaut_database=kclass.db
```
### 3 启动Neo4j服务
neo4j.bat在安装路径bin文件夹下
```bash
.\bin\neo4j.bat console
```
可登录 http://localhost:7474/ 进入Neo4j管理界面
