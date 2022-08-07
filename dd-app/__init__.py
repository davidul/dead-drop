import os

from flask import (Flask, render_template)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    print(app.config)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():  # put application's code here
        return render_template('index.html')

    @app.route('/get/<path>')
    def get_data(path):
        return render_template('retrieve.html', path_id=path)

    from . import db
    db.init_app(app)

    # from . import auth
    # app.register_blueprint(auth.bp)

    from . import drop
    app.register_blueprint(drop.bp)

    return app
