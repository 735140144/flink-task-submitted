"""
@function:
@parameter:
@attention:
"""
from pymongo import MongoClient
import common.AshareConfig as AC
class MongoBase:
    def __init__(self,collection):
        self.collection=collection
        self.OpenDB()
    def OpenDB(self):
        user=AC.MONGO_USER
        passwd=AC.MONGO_PASSWD
        host=AC.MONGO_HOST
        port=AC.MONGO_PORT
        auth_db=AC.MONGO_DB
        uri = "mongodb://"+user+":"+passwd+"@"+host+":"+port+"/"+auth_db+"?authMechanism=SCRAM-SHA-1"
        self.con = MongoClient(uri, connect=False)
        self.db=self.con['ASHARE']
        self.collection=self.db[self.collection]
    def closeDB(self):
        self.con.close()
