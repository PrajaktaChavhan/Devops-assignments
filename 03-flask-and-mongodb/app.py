import os
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB Atlas Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://<username>:<password>@cluster0.mongodb.net/devops_db?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", "devops_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "users")

def get_db():
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=4000)
    return client[DB_NAME]

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "records.json")

# Task 2: Frontend Form & MongoDB Atlas insertion
@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()

        # Validation
        if not name or not email or not course:
            error = "All fields (Full Name, Email, Course) are required."
            return render_template("index.html", error=error, name=name, email=email, course=course)

        try:
            db = get_db()
            users_collection = db[COLLECTION_NAME]
            # Insert document into MongoDB Atlas
            users_collection.insert_one({
                "name": name,
                "email": email,
                "course": course,
                "submitted_at": datetime.utcnow()
            })
            # On success: redirect to success page
            return redirect(url_for("success"))
        except (PyMongoError, ServerSelectionTimeoutError, Exception) as e:
            # On error: display error on the same page without redirection
            error = f"Database Error: Could not connect or insert data into MongoDB Atlas ({str(e)})"
            return render_template("index.html", error=error, name=name, email=email, course=course)

    return render_template("index.html", error=error)

# Task 2: Success Redirection Page
@app.route("/success")
def success():
    return render_template("success.html")

# Task 1: JSON API Route reading from backend file
@app.route("/api", methods=["GET"])
def get_api_data():
    try:
        if not os.path.exists(DATA_FILE):
            return jsonify({"error": "Backend data file not found"}), 404
        
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Return JSON list
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": f"Failed to read backend data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
