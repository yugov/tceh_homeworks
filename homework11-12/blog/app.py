# -*- coding: utf-8 -*-

from flask import Flask, current_app, Blueprint
from views.pages import views
from db import db
import config


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)
    app.register_blueprint(views)
    from models.user import User
    from models.post import Post

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
