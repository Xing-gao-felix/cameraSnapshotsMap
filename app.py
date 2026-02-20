from flask import Flask, jsonify, render_template, send_file
import os


BASE_DIR = os.path.dirname(__file__)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

SNAPSHOT_DIR = os.path.join(BASE_DIR, "snapshots")


CAMERAS = [
    {
        "id": "cam_1",
        "name": "A区左侧入口",
        "zone": "A区",
        "side": "left",
        "nvr_ip": "10.3.132.21",
        "channel": 1,
        "x_ratio": 0.22,
        "y_ratio": 0.45,
    },
    {
        "id": "cam_2",
        "name": "B区主通道",
        "zone": "B区",
        "side": "center",
        "nvr_ip": "10.3.132.21",
        "channel": 2,
        "x_ratio": 0.50,
        "y_ratio": 0.68,
    },
    {
        "id": "cam_3",
        "name": "C区装卸口",
        "zone": "C区",
        "side": "right",
        "nvr_ip": "10.3.132.21",
        "channel": 3,
        "x_ratio": 0.78,
        "y_ratio": 0.52,
    },
]


@app.route("/cameras")
def cameras():
    return jsonify(CAMERAS)


@app.route("/snapshot/<nvr_ip>/<int:channel>")
def snapshot(nvr_ip, channel):
    filename = f"nvr-{nvr_ip}-{channel}.jpg"
    path = os.path.join(SNAPSHOT_DIR, filename)

    if not os.path.exists(path):
        return "No snapshot", 404

    return send_file(path, mimetype="image/jpeg")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
