import controllers.basic

# make the models from our testmogo model available to each of our classes in this file
from models import testmongo

########################################
# NOT FOUND
#  matches .+ endpoint calls (basically any request that wasn't matched by another endpoint)
########################################
class NotFound(controllers.basic.BaseHandler):
  def get(self):
    """
    quick example of rendering html template
    """
    self.render('page_not_found.html')

########################################
# TEST MONGO
#   matches /test/mongo endpoint (will assign the results from the items_in_colleciton function in the models/testmong.py to a variable items_in_collection and then render the value of that variable in an API response [json object])
########################################
class TestMongo(controllers.basic.BaseHandler):
  def get(self):
    """
    quick example of communicating with Mongo
    """
    items_in_collection = testmongo.items_in_collection()
    self.api_response(items_in_collection)
