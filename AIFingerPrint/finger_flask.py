from flask import Flask, request
import tensorflow as tf
import numpy as np
from flask.json import jsonify
import matplotlib.pyplot as plt
import pytesseract
import cv2
import matplotlib
from AIFingerPrint.step5_varify import FingerPrint
matplotlib.use('SVG')

app = Flask(__name__)

@app.route('/finger', methods=['POST', 'GET']) 
def connect():
    isCorrect = ""
    if request.method == 'POST':
        f = request.files['file']
        f.save('./files/' + f.filename)
        print(f.filename)
        try:
            fp = FingerPrint()        
            isCorrect = fp.varify(f.filename)
        finally:
            return isCorrect
    return isCorrect

if __name__ == '__main__':
    app.run(debug=True)
