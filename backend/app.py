from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import base64

from core.functions import *

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submitdata ():
    data = json.loads(request.data)
    if (data == None or 'type' not in data or 'data' not in data):
        resp = jsonify({"message":"fail"})
        resp.status_code = 404
        return resp

    print(data)
    qr = None
    if data['type'] == 'text':
        tmp = base64.b64decode(data['data']['content']).decode()
        qr = genText(tmp)
    elif data['type'] == 'url':
        tmp = base64.b64decode(data['data']['content']).decode()
        qr = genURL(tmp)
    elif data['type'] == 'email':
        tmp = {
            'email':base64.b64decode(data['data']['email']).decode(),
            'subject':base64.b64decode(data['data']['subject']).decode(),
            'mess':base64.b64decode(data['data']['mess']).decode()
        }
        qr = genEmail(email=tmp['email'], subject=tmp['subject'], mess=tmp['mess'])
    elif data['type'] == 'wifi':
        tmp = {
            'network_name':base64.b64decode(data['data']['network_name']).decode(),
            'password':base64.b64decode(data['data']['password']).decode(),
            'encryption':base64.b64decode(data['data']['encryption']).decode()
        }
        qr = genWifi(ssid=tmp['network_name'],password=tmp['password'],type=tmp['encryption'])
    elif data['type'] == 'vcard':
        tmp = {

        }
    # elif data['type'] == 'text':
    # elif data['type'] == 'text':

    if qr == None:
        resp = jsonify({})
        resp.status_code = 404
    else:
        resp = jsonify({"img":qr.decode()})
        resp.status_code = 200
    return resp


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=False)

