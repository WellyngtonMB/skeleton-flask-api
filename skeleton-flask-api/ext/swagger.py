from swagger_ui import flask_api_doc
from config import URL_PREFIX


def init_app(app):
    flask_api_doc(app, config_path='docs/swagger/openapi.yaml',
                  url_prefix=URL_PREFIX + '/doc', title='API skeleton-flask-api')
