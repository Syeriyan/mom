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
    app.run(host="0.0.0.0", port=5000, debug=Truefrom flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to my Flask app!",
        "status": "success"
    })

# About route
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "message": "This is the About page.",
        "status": "success"
    })

# API route
@app.route("/api", methods=["GET"])
def api():
    return jsonify({
        "message": "Hello API",
        "status": "success"
    })

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True))
