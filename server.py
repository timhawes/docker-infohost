#!/usr/bin/env python3

import os
import socket

from flask import Flask, Response, jsonify, request

app = Flask(__name__)

@app.route('<path:subpath>')
def index(subpath):
    data = []
    data.append('path={}'.format(subpath))
    data.append('request.remote_addr={}'.format(request.remote_addr))
    data.append('')
    for k in sorted(os.environ):
        data.append('{}={}'.format(k, os.environ[k]))
    return Response('\n'.join(data) + '\n', mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
