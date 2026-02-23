from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Mock course database
courses = {
    "john": "Backend Engineering",
    "jane": "Frontend Development",
    "bob": "DevOps Fundamentals"
}

@app.route("/user-course/<username>")
def get_user_course(username):
    try:
        # Call user service
        user_response = requests.get(f"http://localhost:5001/users/{username}")
        
        if user_response.status_code == 200:
            user_data = user_response.json()
            course = courses.get(username, "No course assigned")
            
            return jsonify({
                "username": username,
                "name": user_data["name"],
                "course": course,
                "status": "active"
            })
        else:
            return jsonify({"error": "User not found"}), 404
            
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "User service unavailable"}), 503

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "course-service"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)