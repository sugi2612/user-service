from flask import Flask, jsonify, request

app = Flask(_name_)

# Sample data
users = [
    {
        "id": 1,
        "name": "John",
        "email": "john@gmail.com"
    },
    {
        "id": 2,
        "name": "David",
        "email": "david@gmail.com"
    }
]

# Health Check
@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "Running"
    })

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Get user by ID
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# Add new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(user)

    return jsonify(user), 201

# Update user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()

    for user in users:
        if user["id"] == id:
            user["name"] = data["name"]
            user["email"] = data["email"]
            return jsonify(user)

    return jsonify({"message": "User not found"}), 404

# Delete user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify({"message": "User deleted"})

    return jsonify({"message": "User not found"}), 404

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
