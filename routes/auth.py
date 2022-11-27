from re import split
from flask import Blueprint,request,jsonify
from function_jwt import write_token, validate_token

route_auth = Blueprint("route_auth",__name__)

@route_auth.route("/login",methods=['POST'])
def login():
    data = request.get_json()
    if data['email'] == "Guillermo@gmail.com":
        if data['password'] == "memo@qqwe.com":
            return write_token(data)
        else:
            response = jsonify({"message": "incorrect password"})
            response.status_code = 404
            return response
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response

@route_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)