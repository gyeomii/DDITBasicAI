from flask import Flask, request
import tensorflow as tf
import numpy as np
from ai06.ai_module import AI_Module
from flask.json import jsonify
from ai06.memberMBTI import MBTI2

app = Flask(__name__)


@app.route('/recommandReview', methods=['POST', 'GET']) 
def recommandPerson():
    dao = MBTI2()
    rbDao = AI_Module()
    
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "cc"

    print(mem_id)
    userArr = np.zeros(8)
    
    row = dao.selectMemberMBTI(mem_id)
    mbti = row[0]
    
    if mbti[0] == 'E':
        userArr[0] = 1
    if mbti[0] == 'I':
        userArr[1] = 1
    if mbti[1] == 'N':
        userArr[2] = 1
    if mbti[1] == 'S':
        userArr[3] = 1 
    if mbti[2] == 'F':
        userArr[4] = 1
    if mbti[2] == 'T':
        userArr[5] = 1             
    if mbti[3] == 'P':
        userArr[6] = 1
    if mbti[3] == 'J':
        userArr[7] = 1               

    
    
    print(userArr)
    
    
    
    movie1, movie2, movie3 = rbDao.recommandMBTIMovie(userArr)
    
        
    return movie1 +"," + movie2 + "," + movie3

        
if __name__ == '__main__':
    app.run(debug=True)
