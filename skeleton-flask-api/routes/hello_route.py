from flask import Blueprint
from controllers import hello_controller

bp = Blueprint('hello', __name__)


@bp.route('/', methods=['GET'])
def hello():
    return hello_controller.hello()
