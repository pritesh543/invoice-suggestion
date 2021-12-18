from flask import jsonify, request, Blueprint
api = Blueprint('api', __name__)

from db.dbconnect import DataBase

def jsonifyEvents(**kwargs):
    return jsonify({**kwargs, 
                        "success": True, 
                        "message": "Success"
                    })

@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@api.route("/invoice", methods=["POST"])
def invoice():
    if request.method == "POST":
        doc = request.get_json()
        data = DataBase().insert(doc)
        return jsonifyEvents(**data), 200

@api.route("/contact", methods=["PUT"])
def contact():
    if request.method == "PUT":
        doc = request.get_json()
        data = DataBase().update(doc)
        return jsonifyEvents(**data), 200
