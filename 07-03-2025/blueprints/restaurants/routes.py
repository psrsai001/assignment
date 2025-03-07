from flask import Blueprint, jsonify, request

from blueprints.app import db
from blueprints.restaurants.models import Restaurant

restaurants = Blueprint("restaurants", __name__, template_folder="templates")


@restaurants.get("/")
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify(
        [
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "location": restaurant.location,
                "contact_no": restaurant.contact_no,
                "email_id": restaurant.email_id,
            }
            for restaurant in restaurants
        ]
    )


@restaurants.get("/<int:id>")
def get_restaurant_by_id(id: int):
    restaurant = Restaurant.query.get(id)
    if restaurant is not None:
        return jsonify(
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "location": restaurant.location,
                "contact_no": restaurant.contact_no,
                "email_id": restaurant.email_id,
            }
        )
    return jsonify({"message": "Not found"}), 404


@restaurants.post("/")
def post_restaurant():
    data = request.get_json()
    restaurant = Restaurant(**data)
    print(restaurant)
    db.session.add(restaurant)
    db.session.commit()

    return (
        jsonify(
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "location": restaurant.location,
                "contact_no": restaurant.contact_no,
                "email_id": restaurant.email_id,
            }
        ),
        201,
    )
