import os
import tornado.options

tornado.options.define("environment", default="dev", help="environment")

options = {
  'dev' : {
    'mongo_database' : {
      'host' : os.environ['MONGO_HOST'].strip(),
      'port' : os.environ['MONGO_PORT'].strip(),
      'db' : os.environ['MONGO_DB'].strip(),
      'username': os.environ['MONGO_USERNAME'].strip(),
      'password': os.environ['MONGO_PASSWORD'].strip(),
      'directConnection': os.environ['MONGO_DIRECT_CONNECTION'].strip()
    },
  },
  'test' : {
    'mongo_database' : {
      'host' : os.environ['MONGO_HOST'].strip(),
      'port' : os.environ['MONGO_PORT'].strip(),
      'db' : os.environ['MONGO_DB'].strip(),
      'username': os.environ['MONGO_USERNAME'].strip(),
      'password': os.environ['MONGO_PASSWORD'].strip(),
      'directConnection': os.environ['MONGO_DIRECT_CONNECTION'].strip()
    },
  },
  'prod' : {
    'mongo_database' : {
      'host' : os.environ['MONGO_HOST'].strip(),
      'port' : os.environ['MONGO_PORT'].strip(),
      'db' : os.environ['MONGO_DB'].strip(),
      'username': os.environ['MONGO_USERNAME'].strip(),
      'password': os.environ['MONGO_PASSWORD'].strip(),
      'directConnection': os.environ['MONGO_DIRECT_CONNECTION'].strip()
    },
  }
}

default_options = {
  'read_only' : False,
  'max_simultaneous_connections' : 10,
}

def get(key):
  """
  provides ability to get settings values with settings.get('SETTING_YOU_WANT')
  """
  env = tornado.options.options.environment
  if env not in options:
    raise Exception("Invalid Environment (%s)" % tornado.options.options.environment)

  v = options.get(env).get(key) or default_options.get(key)

  if callable(v):
    return v

  if v is not None:
    return v

  return default_options.get(key)

