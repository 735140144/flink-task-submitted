"""
@作者/authpr:千载春秋书风华
@创作日期/createDate:
@版权声明:仅可用于个人学习及学术研究，不可商用。转账和使用需著名出处！
        Can be used for personal study and academic research only,
        not commercial. Transfer and use need famous source!
@Email：735140144@qq.com
Copyright (c) 2022 person All rights reserved.
"""
import socket


class API:
    TUSHARE_TOKEN = '945e12f7dc5e197133193578440a4d3db4f83bd20c0aa641043a9739'


class HOST:

    def __getIp(self):
        """
        @function:获取当前机器的ip地址
        @parameter:null
        @attention:nas:Synology sql:Tencent
        """
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip[:9]

    def tencent(self):
        if self.__getIp() == '10.0.4.6':
            return '127.0.0.1'
        else:
            return 'sql.hhdljt.com'

    def nas(self):
        if self.__getIp() == '172.16.0':
            return '172.16.0.173'
        else:
            return 'nas.hhdljt.com'


MYSQL_PORT = 3306
MYSQL_PORT_STRING = '3306'

HADOOP102_POST = '3306'
HADOOP102_HOST = '172.16.0.101'
HADOOP102_MYSQL_USER = 'root'
HADOOP102_MYSQL_PASSWD = 'Ssymhp12#$'
HADOOP102_DB = 'ASHARE'

TENCENT_HOST = HOST().tencent()
TENCENT_USER = 'root'
TENCENT_PSAAWD = 'Ssymhp12#$'
TENCENT_DB='ASHARE'

NAS_HOST1 = HOST().nas()
NAS_HOST2 = 'nas.hhdljt.com'
NAS_USER = 'root'
NAS_PASSWD = 'ssymhp'

MONGO_HOST = '120.48.27.119'
MONGO_USER = 'root'
MONGO_PASSWD = 'ssymhp'
MONGO_PORT = '27017'
MONGO_DB = 'admin'

DORIS_PORT = '9030'
DORIS_HOST = '172.16.0.101'
DORIS_USER = 'root'
DORIS_PASSWD = 'Ssymhp12#$'
DORIS_DB = 'day_data'