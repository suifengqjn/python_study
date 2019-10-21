#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "qjn19920314", "go1803")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

cursor.execute("SELECT * FROM student")
data = cursor.fetchall()

print("student data")

for d in data:
    print(d)



# 关闭数据库连接
db.close()