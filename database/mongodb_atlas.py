### python -m unittest mongodb_atlas.py
import unittest
from pymongo import MongoClient
from random import randint
# pprint library is used to make the output look more pretty
from pprint import pprint
import sys


class Mongodb_atlas_conn(unittest.TestCase):
    """mongodb atlas connection"""
    db = None
    records = None

    def setUp(self):
        global db, records
        # connect to MongoDB,
        # change the << MONGODB URL >> to reflect your own connection string
        client = MongoClient("mongodb+srv://mongo88:kclkt88@cluster0-mhxgc.azure.mongodb.net/test")
        try:
            db = client.get_database('business')
            records = db.reviews     #get collection object
        except Exception as e:
            print(e)
            sys.exit()

        print('setUp...')

    def tearDown(self):
        """
        Delete the database
        """
        print('tearDown...')

    def test_find_one_doc(self):
        # pprint(records.find_one({'cuisine': 'Italian'}))
        print(records.find_one({'cuisine': 'Italian'}))
        # doc = records.find_one({'cuisine': 'Italian'})
        #
        # doc2 = {k: v for k, v in doc.items() if k.startswith('_id')}
        # print(doc2)
        # records.delete_many(doc2)
        #
        # doc.pop('_id')
        # self.insert_one_doc(doc)
        #
        # # update
        # id = doc.get('_id')
        # self.update_one_doc(id)


    def test_find_docs(self):
        pprint(list(records.find({'name': "Pizza Goat Italian"})))

    def test_insert_one_doc(self):
        review = {
            'name': "Pizza Goat Italian",
            'rating' : randint(1, 9),
            'cuisine': "Italian"
        }
        records.insert_one(review)

    # def test_insert_many_doc(self):
    #     review2 = [
    #         {
    #             'name': "Pizza1 Goat Italian",
    #             'rating': 2,
    #             'cuisine': "Italian"
    #         },
    #         {
    #             'name': "Pizza2 Goat Italian",
    #             'rating': 2,
    #             'cuisine': "Italian"
    #         },
    #     ]
    #     records.insert_many(review2)

    def test_delete_one_doc(self):
        doc = records.find_one({'name': "Pizza Goat Italian"})
        doc2 = {k: v for k, v in doc.items() if k.startswith('_id')}
        records.delete_many(doc2)


    def test_update_one_doc(self):
        doc = records.find_one({'name': "Pizza Goat Italian"})
        
        id = doc.get('_id')
        """ dict.get    vs     dict[key]

        dictionary.get("bogus", default_value)
        returns default_value (whatever you choose it to be), whereas

        dictionary["bogus"]
        would raise a KeyError.

        If omitted, default_value is None, such that

        dictionary.get("bogus")  #  No default specified (defaults to None)
        --- returns None
        """

        result = records.update_one({'_id' : id }, {'$inc': {'rating': 3}})
        print('No. of documents modified : ' + str(result.modified_count))



# db=client.admin
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
