
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hellos World from Platform Engineering!"


@app.route("/health")
def health():
    return {
        "application": "Platform Engineering Demo",
        "status": "UP"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
