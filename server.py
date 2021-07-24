#!/usr/bin/env python3

import platform
import socket

from flask import Flask, Response, jsonify, request

app = Flask(__name__)

@app.route('/<path:subpath>')
def multi(subpath):
    uname = platform.uname()
    data = []
    data.append('system={} node={} release={} version={} machine={}'.format(
        uname.system,
        uname.node,
        uname.release,
        uname.version,
        uname.machine
    ))
    data.append('fqdn={}'.format(socket.getfqdn()))
    data.append('connection from {}'.format(request.remote_addr))
    data.append('')
    data.append('{} {}'.format(request.method, request.full_path))
    for k, v in request.headers.items():
        data.append('{}: {}'.format(k, v))
    return Response('\n'.join(data) + '\n', mimetype='text/plain')

@app.route('/')
def index():
    return multi('')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
