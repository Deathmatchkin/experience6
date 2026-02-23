from flask import Flask, jsonify

app = Flask(__name__)

# Mock user database
users = {
    "john": {"name": "John Doe", "email": "john@example.com"},
    "jane": {"name": "Jane Smith", "email": "jane@example.com"},
    "bob": {"name": "Bob Wilson", "email": "bob@example.com"}
}

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify({
            "username": username,
            "name": users[username]["name"],
            "email": users[username]["email"]
        })
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "user-service"})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
    