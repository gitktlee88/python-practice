from pymongo import MongoClient
import sys

# An important note about collections (and databases) in MongoDB is
# that they are created lazily - none of the above commands have
# actually performed any operations on the MongoDB server.
# **Collections and databases are created when the first document is
# inserted into them.**

class Mongodb_atlas_conn():
    """mongodb atlas connection"""
    db = None
    records = None

    def __init__(self, user='mongo88', pw='kclkt88', dbname='business', coll='reviews'):
        global db, records
        # connect to MongoDB,
        # change the << MONGODB URL >> to reflect your own connection string
        client = MongoClient("mongodb+srv://mongo88:kclkt88@cluster0-mhxgc.azure.mongodb.net/test")
        try:
            # create a database object referencing
            # a new database, called “business”,
            # as follows
            # db = client.business

            db = client.get_database('business')
            collections = db.collection_names()

            colname = locals()
            x = locals().get('coll')

            if x not in collections:
                records = db.create_collection(x)
            else:
                records = db.get_collection(x)

            # print(colname['coll'])
        except Exception as e:
            print(e)
            sys.exit()

    def insert_one_doc(self, name, user, password, category, cdate):
        query = locals()
        del query['self']
        # print(query)
        records.insert_one(query)

    def update_one_doc(self, name, user, password, category, cdate):
        org_query = locals()
        del org_query['self']
        # dictionary comprehension
        query = { k:v for k,v in org_query.items() if k == 'user' }
        new_query = {"$set": org_query}
        records.update_one(query, new_query)

    def delete_one_doc(self, query):
        records.delete_many({query})

    def find_one_doc(self, name, user, password, category):
        query = locals()
        del query['self']
        row = records.find_one(query)
        # print(type(row))
        # print(row)
        lst = []
        if row:
            row.pop('_id')
            lst += [1]
            lv = [v for k, v in row.items()]
            lst += lv
        else:
            lst.append('Not found')
        return lst

    def find_all_docs(self):
        rows = list(records.find({}))
        return rows


    # destructor
    def __del__(self):
        # self.conn.close()
        pass
