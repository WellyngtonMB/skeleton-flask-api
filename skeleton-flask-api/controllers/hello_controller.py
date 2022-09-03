import sys
import datetime
from flask import jsonify
from controllers.errors_controller import errors


def hello():
    try:
        return jsonify(hello="world"), 200
    except Exception as e:
        response = errors(e)
        if response:
            return response
        else:
            return jsonify(msg="Error hello"), 500


