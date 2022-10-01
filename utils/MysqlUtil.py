from sqlalchemy import create_engine
import pymysql
from common import AshareConfig as AC
from utils.MysqlThreadPool import get_my_connection

"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
"""执行语句查询有结果返回结果没有返回0；增/删/改返回变更数据条数，没有返回0"""


class MySqLUtil(object):
    def __init__(self):
        self.db = get_my_connection()  # 从数据池中获取连接

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'inst'):  # 单例
            cls.inst = super(MySqLUtil, cls).__new__(cls, *args, **kwargs)
        return cls.inst

    # 封装执行命令
    def execute(self, sql, param=None, autoclose=False):
        """
        【主要判断是否有参数和是否执行完就释放连接】
        :param sql: 字符串类型，sql语句
        :param param: sql语句中要替换的参数"select %s from tab where id=%s" 其中的%s就是参数
        :param autoclose: 是否关闭连接
        :return: 返回连接conn和游标cursor
        """
        cursor, conn = self.db.getconn()  # 从连接池获取连接
        count = 0
        try:
            # count : 为改变的数据条数
            if param:
                count = cursor.execute(sql, param)
            else:
                count = cursor.execute(sql)
            conn.commit()
            if autoclose:
                self.close(cursor, conn)
        except Exception as e:
            print("error_msg:", e.args)
            pass
        return cursor, conn, count

    # 释放连接
    def close(self, cursor, conn):
        """释放连接归还给连接池"""
        cursor.close()
        conn.close()

    # 查询所有
    def selectall(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
            self.close(cursor, conn)
            return count

    # 查询单条
    def selectone(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            res = cursor.fetchone()
            self.close(cursor, conn)
            return res
        except Exception as e:
            print("error_msg:", e.args)
            self.close(cursor, conn)
            return count

    # 增加
    def insertone(self, sql, param):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            # _id = cursor.lastrowid()  # 获取当前插入数据的主键id，该id应该为自动生成为好
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 增加多行
    def insertmany(self, sql, param):
        """
        :param sql:
        :param param: 必须是元组或列表[(),()]或（（），（））
        :return:
        """
        cursor, conn, count = self.db.getconn()
        try:
            cursor.executemany(sql, param)
            conn.commit()
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 删除
    def delete(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            self.close(cursor, conn)
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 更新
    def update(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count


class PandasMysql:
    def engine_create(self, host, user, passwd, port, db):
        return create_engine('mysql+pymysql://' + user + ':' + passwd + '@' + host + ':' + port + '/' + db)


class Pymysql:
    def __init__(self):
        self.db = pymysql.connect(host=AC.DORIS_HOST,
                                 user=AC.DORIS_USER,
                                 port=19030,
                                 password=AC.DORIS_PASSWD,
                                 db=AC.DORIS_DB,
                                 charset='utf8')

    def readSql(self, sql, params=None):
        connect = self.db
        cur = connect.cursor()
        cur.execute(sql, params)
        fetchall = cur.fetchall()
        cur.close()
        connect.close()
        return fetchall

    def insertSql(self, sql, params=None):
        connect = self.db
        cur = connect.cursor()
        cur.execute(sql, params)
        cur.close()
        connect.close()
        return
    # if __name__ == '__main__':
# db = MySqLHelper()
# TODO查询单条

# TODO 查询多条
# sql1 = "select id,order_id from order_detail"
# args = ('order_detail','80809')
# ret = db.selectall(sql=sql1)
# print(ret)  # (None, b'python', b'123456', b'0')

# TODO 增加单条
# sql2 = 'insert into hotel_urls(cname,hname,cid,hid,url) values(%s,%s,%s,%s,%s)'
# ret = db.insertone(sql2, ('1', '2', '1', '2', '2'))
# print(ret)

# TODO 增加多条
# sql3 = 'insert into userinfo (name,password) VALUES (%s,%s)'
# li = li = [
#     ('分省', '123'),
#     ('到达','456')
# ]
# ret = db.insertmany(sql3,li)
# print(ret)

# TODO 删除
# sql4 = 'delete from  userinfo WHERE name=%s'
# args = 'xxxx'
# ret = db.delete(sql4, args)
# print(ret)

# TODO 更新
# sql5 = r'update userinfo set password=%s WHERE name LIKE %s'
# args = ('993333993', '%old%')
# ret = db.update(sql5, args)
# print(ret)
