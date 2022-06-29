# _*_ coding: utf-8 _*_
# @Time     : 2022/6/28 17:49
# @Author   : Mr_Li
# @FileName : py_test.py
import pymysql  # 导入pymsql模块

connectd = pymysql.connect(host='192.168.1.184',
                           user='root',
                           password='li921204',
                           port=3306,
                           charset='utf8',
                           database='mytest')
"""host：数据库所在服务器IP地址，port：连接数据库端口号，user：连接数据库用户名，password：连接数据库密码，charset：设置字符集
database：所要连接的数据库名称"""
cursor = connectd.cursor(cursor=pymysql.cursors.DictCursor)  # 创建游标
sql = "select * from student"
# sql = "insert into student values('1001','张三','20','一年级一班','男')"  # sql 语句
print(sql)
res = cursor.execute(sql)
print(res)
connectd.commit()  # 提交插入数据
cursor.close()
connectd.close()

'''四、使用 with 简化连接过程
每次都连接关闭很麻烦，使用上下文管理，简化连接过程'''
import pymysql
import contextlib


# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='192.168.1.184', port=3306, user='root', passwd='li921204', database='mytest', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, database=database, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


# 执行sql
with mysql() as cursor:
    print(cursor)
    row_count = cursor.execute("select * from student")
    row_1 = cursor.fetchone()
    print(row_count, row_1)

# import pymysql
#
# # 创建连接
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1', charset='utf8')
# # 创建游标
# cursor = conn.cursor()
#
# # 执行SQL，并返回收影响行数
# effect_row = cursor.execute("select * from tb7")
#
# # 执行SQL，并返回受影响行数
# # effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))
#
# # 执行SQL，并返回受影响行数,执行多次
# # effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
#
#
# # 提交，不然无法保存新建或者修改的数据
# conn.commit()
#
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()
