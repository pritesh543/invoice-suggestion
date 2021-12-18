from fuzzywuzzy import process
from db.dbconnect import DataBase


class Invoice():
    """This class contains the methods
        realted to invoice
    """

    def __init__(self):
        pass
    
    def create_invoice(self, doc):
        """
        creates a invoice in db

        :param:  doc -> dict/json
        :return: invoice id -> dict
        """

        message = DataBase().insert(doc)
        return {"message" : message}

    def update_contact(self, doc):
        """
        updating the contact
        basis unique contact id

        :param:  doc(contact) -> dict
        :return: message -> dict 
        """

        message = DataBase().update(doc)
        return {"message": message}

    def suggest_invoice(self, doc):
        """
        suggesting invoice
        contact name with confidence

        :param:  doc(orgnization, contactName) -> dict
        :return: doc(suggestedContact, confidence) -> dict
        """
        
        filter_query = {"organization" : doc.get("organization")}
        required_fields = {"contact.name": 1, "_id": 0}

        docs = DataBase().find(filter_query, required_fields=required_fields)
        contact_names = [doc.get("contact").get("name") for doc in docs]
        contact_name, confidence = process.extractOne(doc.get("contactName"), set(contact_names))

        return {"suggestedContact": contact_name, "confidence": round(float(confidence/100),2)}