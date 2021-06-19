import requests
from flask import Blueprint, Response
from flask import request, jsonify
from werkzeug.exceptions import BadRequestKeyError

report = Blueprint('report', __name__)


@report.route('/reports', methods=['GET'])
def report_route_get():
    Url = 'http://127.0.0.1:5001/reports'
    # noinspection PyBroadException
    try:
        resp = requests.get(Url)
        Headers = [(name, value) for (name, value) in resp.raw.headers.items()]
        response = Response(resp.content, resp.status_code, Headers)
        return response, 200
    except Exception:
        return jsonify({"error": "Something went wrong"}), 500


@report.route('/report', methods=['GET'])
def reports_route_get():
    Url = 'https://jsonplaceholder.typicode.com/todos/1'
    # noinspection PyBroadException
    try:
        resp = requests.get(Url)
        Headers = [(name, value) for (name, value) in resp.raw.headers.items()]
        response = Response(resp.content, resp.status_code, Headers)
        return response.json
    except Exception:
        return jsonify({"error": "Something went wrong"}), 504


@report.route('/report', methods=['GET'])
def report_route_post():
    errors = report_schema.validate(request.form)
    if errors:
        return jsonify({"error": errors}), 400
    else:
        try:
            f = request.files['file']
            f.save("media/" + f.filename)
            send_file("media/" + f.filename, host='127.0.0.1', port=5001)

            return jsonify({"message": "Your upload request has been submitted"}), 200
        except BadRequestKeyError:
            return jsonify({"error": "No file selected"}), 400
