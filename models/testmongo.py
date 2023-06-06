"""
example of querying to a mongo instance
"""

from models.mongo import db

def items_in_collection():
  return db.test_collection.count_documents({})