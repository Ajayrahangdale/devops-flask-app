from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Ajay! Your DevOps Flask App is Running!"

@app.route("/info")
def info():
    return jsonify({
        "app": "DevOps Flask App",
        "message": "This is your first DevOps project.",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
