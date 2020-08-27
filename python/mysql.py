# -*- coding: UTF-8 -*-
import pymysql
db = pymysql.connect("localhost","root","root","smbms" )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM t_role \
       WHERE id = 2"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        # 打印结果
        print (fname,lname)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()

