"""
@function:
@parameter:
@attention:
"""

import time
from datetime import datetime

from hdfs import *
import flinkcommitconf as conf


def hdfsupload(localpath):
    client = InsecureClient(conf.hdfs_url, user=conf.USER)
    client.upload(conf.hdfs_path, localpath, overwrite=True, cleanup=True)
    return



def hdfscheck(localpath):
    client = InsecureClient(conf.hdfs_url, user=conf.USER)
    client_list = client.list(conf.hdfs_path, status=True)
    name = localpath.split('/')[-1]
    for i in client_list:
        if i[0] == name:
            client.download(conf.hdfs_path + "/" + name, conf.LOCAL_PATH, overwrite=True)
            client.rename(conf.hdfs_path + "/" + name, conf.hdfs_path + "/" + name + datetime.now().strftime("%Y%m%d-%H-%M-%S") + ".bak")
            return "更新时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i[1]["modificationTime"] / 1000))
    return "未找到文件"
