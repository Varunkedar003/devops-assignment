from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>DevOps Technical Assignment</h1>
    <h3>Application Status: Running</h3>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Time: {datetime.datetime.now()}</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevOps Assignment",
        "server": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

