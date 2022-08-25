# lovie/__init__.py
# cd ..
# flask --app lovie --debug run
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'lovie.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that say hello

    @app.route('/test')
    def helloFlask():
        return 'Hello, Flask. <br>This is a message from __init__'
    
    from lovie import db, auth, matabase
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(matabase.bp)
    app.add_url_rule('/', endpoint='index')

    return app
