#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import abort
from flask import jsonify

import json
import logging
import hmac
import os
import requests

from requests.exceptions import ConnectionError

# inlude files
from validate import validate_request

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# Configuration variables
SCALR_SIGNING_KEY = os.getenv('SCALR_SIGNING_KEY', '')
SCALR_WEBHOOK = os.getenv('SCALR_WEBHOOK', '')
SCALR_MYSQL_SERVER = os.getenv('SCALR_MYSQL_SERVER')
SCALR_MYSQL_USER = os.getenv('SCALR_MYSQL_USER')
SCALR_MYSQL_PASS = os.getenv('SCALR_MYSQL_PASS')
SCALR_MYSQL_DB = os.getenv('SCALR_MYSQL_DB')
SCALR_QUERY = os.getenv('SCALR_QUERY')

for var in ['SCALR_SIGNING_KEY', 'SCALR_WEBHOOK']:
    logging.info('Config: %s = %s', var, globals()[var] if 'PASS' not in var else '*' * len(globals()[var]))

@app.route('/' + SCALR_WEBHOOK + '/', methods=['POST', 'GET'])
def webhook_listener():
    if not validate_request(request):
        abort(403)

    mydb = mysql.connector.connect(host=SCALR_MYSQL_SERVER, user=SCALR_MYSQL_USER, passwd=SCALR_MYSQL_PASS, database=SCALR_MYSQL_DB)
    var = mydb.cursor()
    var.execute(SCALR_QUERY)
    json_data=[]
    for (name) in var:
        json_data.append({"value": name[0]})
    out={"list": json_data,"ttl": 3 }
    logging.info(out)
    return jsonify(out)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5018)
