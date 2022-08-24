"""
@function:
@parameter:
@attention:
"""
import utils.MongoUtil


class WirteIntoMongo:
    def WriteIntoMongoWithDeleteAll(sekf, df, ListName):
        try:
            result = df.to_dict(orient='records')
            mongo = utils.MongoUtil.MongoBase(ListName)
            mongo.collection.delete_many({})
            mongo.collection.insert_many(result)
            mongo.closeDB()
            print(ListName + 'has write into mongoDB successfully')
        except Exception as e:
            print(ListName + 'write failed', e.args)

    def WriteIntoMongoWithDeleteAll2(sekf, df, ListName, args):
        try:
            result = df.to_dict(orient='records')
            mongo = utils.MongoUtil.MongoBase(ListName)
            mongo.collection.delete_many({})
            mongo.collection.insert_many(result)
            mongo.closeDB()
            print(ListName + args + 'has write into mongoDB successfully')
        except Exception as e:
            print(ListName + args + 'write failed', e.args)

    def WirteIntoMongo(self, df, ListName):
        try:
            result = df.to_dict(orient='records')
            mongo = utils.MongoUtil.MongoBase(ListName)
            mongo.collection.insert_many(result)
            mongo.closeDB()
            print(ListName + 'has write into mongoDB successfully')
        except Exception as e:
            print(ListName + 'write failed', e.args)

    def WirteIntoMongo2(self, df, ListName, args):
        try:
            result = df.to_dict(orient='records')
            mongo = utils.MongoUtil.MongoBase(ListName)
            mongo.collection.insert_many(result)
            mongo.closeDB()
            print(ListName + args + 'has write into mongoDB successfully')
        except Exception as e:
            print(ListName + args + 'write failed', e.args)
