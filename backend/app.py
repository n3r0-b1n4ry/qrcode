from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submitdata ():
    data = json.loads(request.data)

    print(data)

    if (data == None or 'type' not in data or 'data' not in data):
        resp = jsonify({"message":"fail"})
        resp.status_code = 404
        return resp

    resp = jsonify({"message":"success"})
    resp.status_code = 200
    return resp


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=False)

