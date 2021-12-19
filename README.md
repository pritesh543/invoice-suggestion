
# Data Ingestion & Suggestion (Python, MongoDB, Flask)

This project lets you store you invoice data in the collection and also provide you with the invoice suggestion functionality. \
The services are exposed via REST APIs.





## Installation

You can install this in a docker container or you can download the file and run locally.

(1) docker
```bash
  docker-compose build
  docker-compose up
```

If you don't want to run with docker then.

(2) locally
```bash
  cd invoice-suggestion
  pip install -r requirements.txt
```

## Deployment

```
cd invoice-suggestion
python server.py
```

It runs on 5000 port.



## Documentation

[Design Document](https://github.com/pritesh543/invoice-suggestion/blob/main/Design%20Document.docx)
