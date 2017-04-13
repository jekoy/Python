from datetime import datetime,timedelta
from pymongo import MongoClient
class MongoCache:
    def __init__(self,client=None,expires=timedelta(days=30)):
        self.client=MongoClient('localhost',27017) if client is None else client
        self.db=client.cache
        self.db.webpage.create_index('timestamp',expiresAfterSeconds=expires.total_seconds())

    def __getitem__(self,url):
        recond=self.db.webpage.find_one({'_id': url})
        if record:
            return record['result']
        else:
            raise KeyError(url+'does not exists')
    def __setitem__(self,url,result):
        record={'result':result,'timestamp':datetime.utcnow()}
        self.da.webpage.update({'_id':url},{'$set':record},upsert=True)
