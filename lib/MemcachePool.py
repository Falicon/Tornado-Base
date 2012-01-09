import pylibmc
import Queue

import settings

def servers():
  return settings.get('memcached')

# num of bax cached connections; not num of open connections
server_pool = Queue.Queue(maxsize=50)

def newConnection():
  """
  set up a new memcached connection
  """
  if callable(servers):
    return pylibmc.Client(servers())
  else:
    return pylibmc.Client(servers)

def pool(targetFunction):
  """
  decorator implements a self growing pool.
  returns connections to it.
  if no connection, create one.
  if cant return connection, drop it.
  """
  def acquireAndRelease(*args, **kwargs):
    try:
      conn = server_pool.get_nowait()
    except Queue.Empty:
      conn = newConnection()
    val = None
    try:
      try:
        val = targetFunction(conn, *args, **kwargs)
      except:
        val = None
    finally:
      try:
        server_pool.put_nowait(conn)
      except Queue.Full:
        pass
    return val
  return acquireAndRelease

class PoolClient(object):
  def __getattribute__(self, name):
    @pool
    def wrapperFunction(*args, **kwargs):
      return getattr(args[0], name)(*args[1:], **kwargs)
    return wrapperFunction
    
mc = PoolClient()