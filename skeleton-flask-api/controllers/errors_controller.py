from flask import jsonify
from werkzeug.exceptions import HTTPException


def errors(e):
    if isinstance(e, KeyError):
        return jsonify(msg="Missing required fields"), 400
    elif isinstance(e, HTTPException):
        if e.code == 400:
            return jsonify(msg="Bad request"), 400
        elif e.code == 403:
            return jsonify(msg="Forbidden"), 403
        elif e.code == 404:
            return jsonify(msg="Not found"), 404
        elif e.code == 405:
            return jsonify(msg="Method not allowed"), 405
        elif e.code == 500:
            return jsonify(msg="Internal server error"), 500
        else:
            return False
    else:
        False
