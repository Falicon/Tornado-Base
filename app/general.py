import app.basic

from lib import testmongo

class NotFound(app.basic.BaseHandler):

  def get(self):
    """
    quick example of rendering html template
    """
    self.render('page_not_found.html')

class TestMongo(app.basic.BaseHandler):

  def get(self):
    """
    quick example of communicating with Mongo
    """
    items_in_collection = testmongo.items_in_collection()
    self.api_response(items_in_collection)