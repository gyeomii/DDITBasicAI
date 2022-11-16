from flask import Flask, request
import tensorflow as tf
import numpy as np
from ai04.mbti_book import MBTI
from ai04.ai_module import AI_Module4

app = Flask(__name__)


@app.route('/recommandMBTI', methods=['POST', 'GET']) 
def recommandPerson():
    dao = MBTI()
    rbDao = AI_Module4()
    row = dao.selectMBTI('jyp')
    userArr = np.zeros(8)
    print(row[2])
    a=list(row[2])
    print(a)

    if a[0]=='I':
        userArr[0]=1
    elif a[0]=='E':
        userArr[1]=1


    if a[1]=='N':
        userArr[2]=1
    elif a[1]=='S':
        userArr[3]=1


    if a[2]=='F':
        userArr[4]=1
    elif a[2]=='T':
        userArr[5]=1


    if a[3]=='P':
        userArr[6]=1
    elif a[3]=='J':
        userArr[7]=1

    print(userArr)
    
    book1, book2, book3 = rbDao.recommandBook(userArr)
    
        
    return book1 +"," + book2 + "," + book3

        
if __name__ == '__main__':
    app.run(debug=True)
