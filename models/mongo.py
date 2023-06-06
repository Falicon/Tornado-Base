import logging
import pymongo
import settings

class Proxy(object):
  _db = None
  def __getattr__(self, name):
    if Proxy._db == None:
      mongo_database = settings.get('mongo_database')

      connection = pymongo.MongoClient(
        'mongodb://%s:%s@%s:%s/%s?authSource=admin&directConnection=%s' % (
          mongo_database['username'],
          mongo_database['password'],
          mongo_database['host'],
          mongo_database['port'],
          mongo_database['db'],
          mongo_database['directConnection']
        ),
        connectTimeoutMS=1000
      )

      Proxy._db = connection[mongo_database['db']]

    return getattr(self._db, name)

db = Proxy()