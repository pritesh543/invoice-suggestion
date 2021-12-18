from flask import jsonify, request, Blueprint
api = Blueprint('api', __name__, url_prefix="/api/")

from controller import Invoice

def jsonifyEvents(**kwargs):
    return jsonify({**kwargs})

@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@api.route("/invoice", methods=["POST"])
def invoice():
    doc = request.get_json()
    
    data = Invoice().create_invoice(doc)
    return jsonifyEvents(**data), 200


@api.route("/contact", methods=["PUT"])
def contact():
    doc = request.get_json()
    
    data = Invoice().update_contact(doc)
    return jsonifyEvents(**data), 200


@api.route("/suggest/invoice", methods=["GET"])
def suggest_invoice():
    doc = request.get_json()
    
    data = Invoice().suggest_invoice(doc)
    return jsonifyEvents(**data), 200