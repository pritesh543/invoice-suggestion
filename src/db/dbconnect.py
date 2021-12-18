import os
import configparser
from pymongo import MongoClient

# reading params from config
config_path = os.path.join(os.getcwd(), "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

# mongodb url
dburl = "mongodb://{host}:{port}/".\
            format(host=config["database"]["host"],\
                    port=int(config["database"]["port"]))


class DataBase:
    """This class connect to the database & 
    performs all the DB operations at a single place
    """

    def __init__(self):
        """

        setting up mongodb server credentials
        to connect to the database
        """

        self.client = MongoClient(dburl) # configure db url
        self.db = self.client[config["database"]["db"]] # configure db name
        self.collection = config["database"]["collection"]

    def find(self, criteria, required_fields=None):
        """

        search in the collection with
        requisited filter and required fields 
        required in the output
        """

        if required_fields:
            cursor = self.db[self.collection].find(criteria, required_fields)
        else:
            cursor = self.db[self.collection].find(criteria)

        docs = [doc for doc in cursor]
        return docs

    def insert(self, document):
        """
        
        insert the document in the database
        (for bulk insert we can use insert_many)
        """
        try:
            self.db[self.collection].insert_one(document)
            return "Record Succesfully Inserted"
        except Exception as e:
            return str(e)

    def update(self, document):
        """

        updating the contact attributes
        inside an invoice object        
        """

        criteria = {"contact._id" : document.get("_id")}
        set_object = {"$set" : {"contact": document}}
        
        updated = self.db[self.collection].update_one(criteria, set_object)
        if updated.matched_count > 0:
            return "Record Succesfully Updated"