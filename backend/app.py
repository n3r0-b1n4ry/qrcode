from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import base64
import hashlib
import datetime

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
    result = None
    h = hashlib.md5()
    h.update((request.remote_addr + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")).encode())

    qr = genQR(os.path.join(TMPPATH, '{}'.format(h.hexdigest())))

    if data['type'] == 'text':
        tmp = base64.b64decode(data['data']['content']).decode("utf16")
        result = qr.genText(data=tmp)
    elif data['type'] == 'url':
        tmp = base64.b64decode(data['data']['content']).decode("utf16")
        if 'http://' not in tmp or 'https://' not in tmp:
            tmp = 'http://'+ tmp
        result = qr.genURL(data=tmp)
    elif data['type'] == 'email':
        tmp = {
            'email':base64.b64decode(data['data']['email']).decode(),
            'subject':base64.b64decode(data['data']['subject']).decode(),
            'mess':base64.b64decode(data['data']['mess']).decode()
        }
        result = qr.genEmail(email=tmp['email'], subject=tmp['subject'], mess=tmp['mess'])
    elif data['type'] == 'wifi':
        tmp = {
            'network_name':base64.b64decode(data['data']['network_name']).decode(),
            'password':base64.b64decode(data['data']['password']).decode(),
            'encryption':base64.b64decode(data['data']['encryption']).decode()
        }
        result = qr.genWifi(ssid=tmp['network_name'],password=tmp['password'],type=tmp['encryption'])
    elif data['type'] == 'vcard':
        tmp = {
            'firstname':base64.b64decode(data['data']['fname']).decode(),
            'lastname':base64.b64decode(data['data']['lname']).decode(),
            'fullname':"{} {}".format(base64.b64decode(data['data']['lname']).decode(), base64.b64decode(data['data']['fname']).decode()),
            'organize':base64.b64decode(data['data']['company_ch']).decode(),
            'addr':"{} {}".format(base64.b64decode(data['data']['street']).decode(), base64.b64decode(data['data']['state']).decode()),
            'city':base64.b64decode(data['data']['city']).decode(),
            'taxcode':base64.b64decode(data['data']['zip']).decode(),
            'country':base64.b64decode(data['data']['country']).decode(),
            'phonenumber':base64.b64decode(data['data']['mobile']).decode(),
            'email':base64.b64decode(data['data']['email']).decode(),
            'website':base64.b64decode(data['data']['website']).decode()
        }
        result = qr.genVcard(data=tmp)
    # elif data['type'] == 'text':
    # elif data['type'] == 'text':

    del qr
    if result == None:
        resp = jsonify({})
        resp.status_code = 404
    else:
        resp = jsonify({"img":result.decode()})
        resp.status_code = 200
    return resp


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=False)

