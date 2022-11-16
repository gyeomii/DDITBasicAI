from flask import Flask, request
import tensorflow as tf
import numpy as np
from flask.json import jsonify
import matplotlib.pyplot as plt
import pytesseract
import cv2
import matplotlib
from AIStupid.recognitionOfBookNumber import StupidBook
from AIHeight.checkHeight import height
app = Flask(__name__)

@app.route('/stupid', methods=['POST', 'GET']) 
def connect():
    bookNum = ["인식불가"]
    camNum = "200"
    book = ""
    if request.method == 'POST':
        f = request.files['file']
        f.save('./files/' + f.filename)
        print(f.filename)
        try:
            sb = StupidBook()
            bookNum = sb.stupid(f.filename, camNum)
            bookNum.append(camNum)
            print(bookNum)
        finally:
            for i in range(len(bookNum)):
                book += bookNum[i] + ","
            print(book)
            return book
                
    return book

@app.route('/height', methods=['POST', 'GET']) 
def height2():
    result=""
    if request.method == 'POST':
        f = request.files['file']
        f.save('../AIHeight/files/' + f.filename)
        print(f.filename)
        try:
            he = height()
            result = he.height(f.filename)
        finally:
            return result
                
    return result

if __name__ == '__main__':
    app.run(debug=True)