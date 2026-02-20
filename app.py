# app.py
from flask import Flask, jsonify, render_template_string, send_file
from flask import render_template
import os


BASE_DIR = os.path.dirname(__file__)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
print("BASE_DIR =", BASE_DIR)
print("TEMPLATE FOLDER =", app.template_folder)
print("STATIC FOLDER =", app.static_folder)
print("FILES IN TEMPLATE FOLDER =", os.listdir(app.template_folder) if os.path.exists(app.template_folder) else "NOT EXISTS")


SNAPSHOT_DIR = os.path.join(BASE_DIR, "snapshots")

@app.route("/cameras")
def cameras():
    return jsonify([
        {
            "id": "cam_1",
            "nvr_ip": "10.3.132.21",
            "channel": 1,
            "x": 320,
            "y": 260
        },
        {
            "id": "cam_2",
            "nvr_ip": "10.3.132.21",
            "channel": 2,
            "x": 580,
            "y": 410
        },
        {
            "id": "cam_3",
            "nvr_ip": "10.3.132.21",
            "channel": 3,
            "x": 760,
            "y": 300
        }
    ])

@app.route("/snapshot/<nvr_ip>/<int:channel>")
def snapshot(nvr_ip, channel):
    filename = f"nvr-{nvr_ip}-{channel}.jpg"
    path = os.path.join(SNAPSHOT_DIR, filename)

    if not os.path.exists(path):
        return "No snapshot", 404

    return send_file(path, mimetype="image/jpeg")

# @app.route("/")
# def index():
#     return render_template_string("<h1>OK - Flask route works</h1>")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)