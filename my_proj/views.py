from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)



@app.route("/")
def hello_page():
    return f"<a href='/healthcheck'>healthcheck page</a>"


@app.route("/healthcheck")
def healthcheck():
    response = jsonify(date=datetime.now(), status="OK")
    response.status_code = 200
    return response
