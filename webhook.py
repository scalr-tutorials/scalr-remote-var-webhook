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
SCALR_JSONFILE = os.getenv('SCALR_JSONFILE')

for var in ['SCALR_SIGNING_KEY', 'SCALR_WEBHOOK']:
    logging.info('Config: %s = %s', var, globals()[var] if 'PASS' not in var else '*' * len(globals()[var]))

@app.route('/' + SCALR_WEBHOOK + '/', methods=['POST', 'GET'])
def webhook_listener():
    logging.info(request)
    if not validate_request(request, SCALR_SIGNING_KEY):
        abort(403)
    out=json.load(open(SCALR_JSONFILE))
    logging.info(out)
    return jsonify(out)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5018)
