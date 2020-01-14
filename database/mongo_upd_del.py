from pymongo import MongoClient
from random import randint
#include pprint for readabillity of the
from pprint import pprint


# #Step 1: Connect to MongoDB - Note: Change connection string as needed
# client = MongoClient(port=27017)
client = MongoClient("mongodb+srv://mongo88:kclkt88@cluster0-mhxgc.azure.mongodb.net/test")

db=client.business

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)

# Deleting documents
result = db.restaurants.delete_many({"category": "Bar Food"})
print('\ncategory: Bar Food was deleted')
## If you are deleting a large number of documents it may be
## more efficient to drop the collection instead of deleting all
## the documents.
