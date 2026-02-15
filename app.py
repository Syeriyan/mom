from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Flask app!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/api")
def api():
    return jsonify({"message": "Hello API", "status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
