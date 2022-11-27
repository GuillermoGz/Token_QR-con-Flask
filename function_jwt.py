from jwt import encode,decode
from jwt import exceptions
from os import getenv
from datetime import datetime , timedelta
from flask import jsonify,send_file
import qrcode

def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data,"exp": expire_date(1)},
                   key=getenv('SECRET'),algorithm='HS256')
    return crear_qr(token.encode("UTF-8"))

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv('SECRET'),algorithms=['HS256'])
        decode(token, key=getenv('SECRET'),algorithms=['HS256'])
    except exceptions.DecodeError:
        response = jsonify({"message":"Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message":"Token Expired"})
        response.status_code = 401
        return response

def crear_qr(data):
    input = data
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(input)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')
    img.save("c:/Users/guill/Desktop/Flask/img_tokens/"+str(data)+".jpeg")
    return send_file("c:/Users/guill/Desktop/Flask/img_tokens/"+str(data)+".jpeg",mimetype="image/jpeg")
