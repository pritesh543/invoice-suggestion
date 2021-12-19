import sys
import json
import unittest
from dummy_data import *
from server import app

headers = {
            'Content-Type': 'application/json'
          }

def parse_response(response):
    return response.get_json()

class TestInvoiceAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_create_invoice(self):
        payload = json.dumps(invoice_document)
        response = self.app.post("/api/invoice", headers=headers, data=payload)
        response = parse_response(response)
        
        self.assertEqual(response['message'], 'Record Succesfully Inserted')

    def test_update_invoice_contact(self):
        payload = json.dumps(contact_document)
        response = self.app.put("/api/contact", headers=headers, data=payload)
        response = parse_response(response)
        
        self.assertEqual(response['message'], 'Record Succesfully Updated')     

    def test_update_suggest_invoice(self):
        payload = json.dumps(suggest_invoice_document)
        response = self.app.get("/api/suggest/invoice", headers=headers, data=payload)
        response = parse_response(response)

        self.assertEqual(response['confidence'], 0.9)
        self.assertEqual(response['suggestedContact'].lower(), 'RAY'.lower())