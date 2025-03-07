from flask import Blueprint, jsonify, request

from blueprints.app import db
from blueprints.items.models import Item
from blueprints.restaurants.models import Restaurant

items = Blueprint("items", __name__, template_folder="templates")


@items.get("/")
def get_items():
    items = Item.query.all()
    return jsonify(
        [
            {
                "id": item.id,
                "name": item.name,
                "unit": item.unit,
                "price": item.price,
                "category": item.category,
                "restaurant_id": item.restaurant_id,
            }
            for item in items
        ]
    )


@items.get("/<int:id>")
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(
        {
            "id": item.id,
            "name": item.name,
            "unit": item.unit,
            "price": item.price,
            "category": item.category,
            "restaurant_id": item.restaurant_id,
        }
    )


@items.post("/")
def add_item():
    data: dict[str, str | int | float] = request.get_json()

    restaurant_id = data.get("restaurant_id", None)
    if restaurant_id is None:
        return jsonify({"message": "Restaurant_id not found"}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant is None:
        return jsonify({"message": "Restaurant_id not found"}), 404

    new_item = Item(**data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added successfully", "id": new_item.id}), 201


@items.put("/<int:id>")
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify({"message": "Item updated successfully"})


@items.delete("/<int:id>")
def delete_item(id):
    item = Item.query.get(id)
    if item is None:
        return jsonify({"message": "item with given id not found"}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})
