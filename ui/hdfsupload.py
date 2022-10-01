"""
@function:
@parameter:
@attention:
"""

from hdfs import *
import time
import flinkcommitconf as conf


def hdfsupload(localpath):
    client = InsecureClient(conf.hdfs_url, user='root')
    client.upload(conf.hdfs_path, localpath, overwrite=True, cleanup=True)
    return


def hdfscheck(localpath):
    client = InsecureClient(conf.hdfs_url, user='root')
    client_list = client.list("/project",status=True)
    name = localpath.split('/')[-1]
    for i in client_list:
        if i[0]== name:
            return "更新时间："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i[1]["modificationTime"]/1000))
    return "未找到文件"
