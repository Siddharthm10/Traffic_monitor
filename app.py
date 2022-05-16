from flask import Flask, render_template, url_for, Response, request, redirect,session
from flask_socketio import SocketIO, emit
import cv2
import base64
from src.yolo_video import Traffic_analyser
import numpy as np
import json
from src.input_retrieval import *

app = Flask(__name__)
socketio = SocketIO(app)
Upload_dir = "testset"
app.secret_key = "RandomString123"
Upload_dir = 'testset/'
app.config["SESSION_PERMANENT"] = False

@app.route('/render')
def home():
    summary = {}
    with open("log.json", "r+") as f:
        summary = json.load(f)
    return render_template("index.html",summary=summary)

@app.route('/feed')
def feed():
    return Response(Traffic_analyser(session['filename']), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/', methods=["POST", "GET"])
def uploader():
    if request.method=="POST":
        f = request.files['file']
        if(f):
            filename = os.path.join(Upload_dir, f.filename)
            session["filename"] = filename
            f.save(filename)
        else:
            session["filename"] = os.path.join(Upload_dir, "bridge.mp4")
        return redirect(url_for('home'))

    with open("log.json", "r+") as f:
        summary = json.load(f)

    return render_template("upload.html",summary=summary)


if __name__=='__main__':
    import numpy as np
    import cv2
    from src.input_retrieval import *

    socketio.run(app,port=4000, debug=True)