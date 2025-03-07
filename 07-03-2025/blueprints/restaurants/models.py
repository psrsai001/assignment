from blueprints.app import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    items = db.relationship("Item", backref="restaurant", lazy=True)
