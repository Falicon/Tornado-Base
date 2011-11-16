import tornado.options

tornado.options.define("environment", default="dev", help="environment")

options = {
  'dev' : {
    'mongo_database' : {'host' : 'localhost', 'port' : 27017, 'db' : 'dev'},
  },
  'test' : {
    'mongo_database' : {'host' : '', 'port' : 27017, 'db' : ''},
  },
  'prod' : {
    'mongo_database' : {'host' : '', 'port' : 27017, 'db' : ''},
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

