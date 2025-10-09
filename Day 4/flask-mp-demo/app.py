# app.py
from flask import Flask, jsonify, request
import repo
import services

app = Flask(__name__)

@app.get("/users/<int:user_id>")
def get_user(user_id: int):
    user = repo.get_user(user_id)
    if not user:
        return jsonify({"error": "not found"}), 404
    return jsonify(user)

@app.post("/orders")
def create_order():
    """
    Payload:
    {
      "user_id": 1,
      "items": [{"sku":"ABC","qty":2,"price":10.0}, ...]
    }
    """
    data = request.get_json(force=True)
    user_id = data.get("user_id")
    items = data.get("items", [])
    if not user_id or not isinstance(items, list) or not items:
        return jsonify({"error": "invalid payload"}), 400

    # Check user exists (DB)
    user = repo.get_user(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    # Price items (external service)
    quote = services.get_quote(items)

    # Save order (DB)
    order = repo.save_order(user_id, items)

    return jsonify({
        "order": order,
        "pricing": quote,
        "user_tier": user["tier"],
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
