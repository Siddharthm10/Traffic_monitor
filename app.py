from flask import Flask, render_template, url_for, Response
from flask_socketio import SocketIO, emit
import cv2
import base64
from src.yolo_video import Traffic_analyser
import numpy as np
from src.input_retrieval import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/feed')
def feed():
    return Response(Traffic_analyser(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__=='__main__':
    import numpy as np
    import imutils
    import time
    from scipy import spatial
    import cv2
    from src.input_retrieval import *


    socketio.run(app, debug=True)