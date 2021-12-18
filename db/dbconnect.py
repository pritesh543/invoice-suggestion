import os
import configparser
from pymongo import MongoClient

config_path = os.path.join(os.getcwd(), "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

# db url
dburl = "mongodb://{host}:{port}/".\
            format(host=config["database"]["host"],\
                    port=int(config["database"]["port"]))

class DataBase:
    def __init__(self):
        self.client = MongoClient(dburl) # configure db url
        self.db = self.client[config["database"]["db"]] # configure db name
        self.collection = config["database"]["collection"]

    def find(self, _id):
        docs = self.db[self.collection].find_one({"contact._id": _id})
        return {"data": docs}

    def insert(self, document):
        inserted = self.db[self.collection].insert_one(document)
        return {"_id" : str(inserted.inserted_id)}

    def update(self, document):
        criteria = {"contact._id" : document.get("_id")}
        set_object = {"$set" : {"contact": document}}
        
        updated = self.db[self.collection].update_one(criteria, set_object)
        if updated.matched_count > 0:
            return {"message": "Record Succesfully Updated"}
