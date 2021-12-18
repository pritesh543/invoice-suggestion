import random

from api import invoice, suggest_invoice
invoice_number = "invoice-{}".format(random.randint(0,1000))

invoice_document={
            "_id": invoice_number,
            "organization": "Zeta",
            "createdAt": "2021-12-18T10:53:31.339Z",
            "updatedAt": "2021-12-19T19:45:19.500Z",
            "amount": {
                "currencyCode": "EUR",
                "value": 50.3
            },
            "contact": {
                "_id": "contact05",
                "iban": "DE88100500001310030013243",
                "name": "Kim",
                "organization": "Zeta"
            },
            "invoiceDate": "2021-12-18T00:00:00.000Z",
            "invoiceId": "VR210230010"
        }

contact_document={
            "_id": "contact05",
            "iban": "DE881005000013100300XXXX",
            "name": "RAY",
            "organization": "TomH"
        }

suggest_invoice_document = {
            "organization": "Zeta",
            "contactName": "RA"
        }