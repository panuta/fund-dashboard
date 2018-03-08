from flask import Flask
from sassutils.wsgi import SassMiddleware


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    # initialize_extensions(app)
    register_blueprints(app)

    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        'project': ('static/scss', 'static/css', '/static/css'),
    })
    return app


def register_blueprints(app):
    from project.dashboard import dashboard_blueprint

    app.register_blueprint(dashboard_blueprint)
