
from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import uuid, os
from chatbot import AdikhiChatbot
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "adikhi-secret-2024")
CORS(app)

# 🔹 Temporary user storage
users = {}

# 🔹 Session bots
sessions = {}

def get_bot() -> AdikhiChatbot:
    if "sid" not in session:
        session["sid"] = str(uuid.uuid4())

    sid = session["sid"]

    if sid not in sessions:
        sessions[sid] = AdikhiChatbot()

    return sessions[sid]


# 🔹 Landing Page
@app.route("/")
def home():
    return render_template("landing.html")


# 🔹 Chat Page (PROTECTED)
@app.route("/chat")
def chat_page():
    if "user" not in session:
        return render_template("landing.html")
    return render_template("index.html")


# 🔹 Signup
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"error": "User already exists"})

    users[username] = password
    return jsonify({"message": "Signup successful"})


# 🔹 Login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        session["user"] = username
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"})


# 🔹 Chat API
@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        message = request.json["message"]

        bot = get_bot()
        reply = bot.chat(message)

        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "⚠️ Backend error"})


# 🔹 Reset
@app.route("/api/reset", methods=["POST"])
def reset():
    get_bot().reset()
    return jsonify({"ok": True})


# 🔹 Stats
@app.route("/api/stats")
def stats():
    return jsonify(get_bot().stats())


if __name__ == "__main__":
    print("\n" + "★" * 55)
    print("  🤖  Adikhi AI — Business Intelligence Chatbot")
    print("  🌐  Open: http://localhost:5000")
    print("★" * 55 + "\n")

    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

