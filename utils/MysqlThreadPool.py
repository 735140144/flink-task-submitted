"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
from DBUtils.PooledDB import PooledDB
import common.MysqlConfig as Config

"""
@功能：创建数据库连接池
"""


class MyConnectionPool(object):
    __pool = None

    # def __init__(self):
    #     self.conn = self.__getConn()
    #     self.cursor = self.conn.cursor()

    # 创建数据库连接conn和游标cursor
    def __enter__(self):
        self.conn = self.__getconn()
        self.cursor = self.conn.cursor()

    # 创建数据库连接池
    def __getconn(self):
        if self.__pool is None:
            self.__pool = PooledDB(
                creator=Config.DB_CREATOR,
                mincached=Config.DB_MIN_CACHED,
                maxcached=Config.DB_MAX_CACHED,
                maxshared=Config.DB_MAX_SHARED,
                maxconnections=Config.DB_MAX_CONNECYIONS,
                blocking=Config.DB_BLOCKING,
                maxusage=Config.DB_MAX_USAGE,
                setsession=Config.DB_SET_SESSION,
                host=Config.DB_TEST_HOST,
                port=Config.DB_TEST_PORT,
                user=Config.DB_TEST_USER,
                passwd=Config.DB_TEST_PASSWORD,
                db=Config.DB_TEST_DBNAME,
                use_unicode=False,
                charset=Config.DB_CHARSET
            )
        return self.__pool.connection()

    # 释放连接池资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    # 关闭连接归还给链接池
    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()

    # 从连接池中取出一个连接
    def getconn(self):
        conn = self.__getconn()
        cursor = conn.cursor()
        return cursor, conn


# 获取连接池,实例化
def get_my_connection():
    return MyConnectionPool()