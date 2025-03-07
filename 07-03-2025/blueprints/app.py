from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./home_food.db"
    db.init_app(app)

    # imports and register all blueprints

    from blueprints.items.routes import items
    from blueprints.restaurants.models import Restaurant
    from blueprints.restaurants.routes import restaurants

    app.register_blueprint(items, url_prefix="/items")
    app.register_blueprint(restaurants, url_prefix="/restaurants")

    migrate = Migrate(app, db)
    return app
