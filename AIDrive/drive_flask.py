from flask import Flask, request
import tensorflow as tf
import numpy as np
from flask.json import jsonify
import matplotlib.pyplot as plt
import pytesseract
import cv2
import matplotlib
from AIDrive.drive import Drive
matplotlib.use('SVG')

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET']) 
def connect():

    carNum = "인식불가"    
    if request.method == 'POST':
        f = request.files['file']
        f.save('./files/' + f.filename)
        print(f.filename)
        try:
            de = Drive()        
            carNum = de.carNum(f.filename)
        finally:
            return carNum
    return carNum

if __name__ == '__main__':
    app.run(debug=True)
