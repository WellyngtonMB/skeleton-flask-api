from flask import Flask


def create_app():
    from ext import swagger, cors
    
    from routes.hello_route import bp as hello_bp
    
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    swagger.init_app(app)
    cors.init_app(app)
        
    app.register_blueprint(hello_bp, url_prefix=app.config['URL_PREFIX']+'/hello')

    # print(app.config)
    return app
