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
        tmp = base64.b64decode(data['data']['content']).decode("latin_1")
        result = qr.genText(data=tmp)
    elif data['type'] == 'url':
        tmp = base64.b64decode(data['data']['content']).decode("latin_1")
        if 'http://' not in tmp or 'https://' not in tmp:
            tmp = 'http://'+ tmp
        result = qr.genURL(data=tmp)
    elif data['type'] == 'email':
        tmp = {
            'email':base64.b64decode(data['data']['email']).decode('latin_1'),
            'subject':base64.b64decode(data['data']['subject']).decode('latin_1'),
            'mess':base64.b64decode(data['data']['mess']).decode('latin_1')
        }
        result = qr.genEmail(email=tmp['email'], subject=tmp['subject'], mess=tmp['mess'])
    elif data['type'] == 'wifi':
        tmp = {
            'network_name':base64.b64decode(data['data']['network_name']).decode('latin_1'),
            'password':base64.b64decode(data['data']['password']).decode('latin_1'),
            'encryption':base64.b64decode(data['data']['encryption']).decode('latin_1')
        }
        result = qr.genWifi(ssid=tmp['network_name'],password=tmp['password'],type=tmp['encryption'])
    elif data['type'] == 'vcard':
        tmp = {
            'firstname':base64.b64decode(data['data']['fname']).decode('latin_1'),
            'lastname':base64.b64decode(data['data']['lname']).decode('latin_1'),
            'fullname':"{} {}".format(base64.b64decode(data['data']['lname']).decode('latin_1'), base64.b64decode(data['data']['fname']).decode('latin_1')),
            'organize':base64.b64decode(data['data']['company_ch']).decode('latin_1'),
            'addr':"{} {}".format(base64.b64decode(data['data']['street']).decode('latin_1'), base64.b64decode(data['data']['state']).decode('latin_1')),
            'city':base64.b64decode(data['data']['city']).decode('latin_1'),
            'taxcode':base64.b64decode(data['data']['zip']).decode('latin_1'),
            'country':base64.b64decode(data['data']['country']).decode('latin_1'),
            'phonenumber':base64.b64decode(data['data']['mobile']).decode('latin_1'),
            'email':base64.b64decode(data['data']['email']).decode('latin_1'),
            'website':base64.b64decode(data['data']['website']).decode('latin_1')
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

