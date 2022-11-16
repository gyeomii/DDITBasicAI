from flask import Flask, request
import tensorflow as tf
import numpy as np
from ai02.ai_module import AI_Module2
from ai02.getBookNoAndKdcNo import getBookNo
from flask.json import jsonify

app = Flask(__name__)


@app.route('/recommandRecord', methods=['POST', 'GET']) 
def recommandRecord():
    kdcDao = getBookNo()
    rbDao = AI_Module2()
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "aa"

    print(mem_id)
    row = kdcDao.selectBookNoOfMember(mem_id)
    userArr = row
    print(userArr)
    book1, book2, book3 = rbDao.recommandBook(userArr)
    return book1 +"," + book2 + "," + book3

        
if __name__ == '__main__':
    app.run(debug=True)
