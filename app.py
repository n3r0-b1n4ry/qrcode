from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submitdata ():
    data = json.loads(request.data)

    if (data == None or 'type' not in data or 'data' not in data):
        resp.status_code = 404
        return resp

    resp = jsonify({"type":data["type"]})
    resp.status_code = 200
    return resp


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=False)

