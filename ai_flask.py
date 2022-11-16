from flask import Flask, request, render_template, json
from flask.json import jsonify
import numpy as np
from ai01.ageGenderInterest import AGI
from ai01.ai_module import AI_Module1
from ai02.ai_module import AI_Module2
from ai02.getBookNoAndKdcNo import getBookNo
from ai04.mbti_book import MBTI
from ai04.ai_module import AI_Module4
from ai05.movieLinkRating import MOR
from ai05.ai_module import AI_Module5
from ai06.ai_module import AI_Module6
from ai06.memberMBTI import MBTI2
from ai03.ai_module import AI_Module3
from ai03.celebBook import celebBook
app = Flask(__name__)


@app.route('/recommandPersonal', methods=['POST', 'GET']) 
def recommandPerson():
    agiDao = AGI()
    rbDao = AI_Module1()
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "aa"
    row = agiDao.selectMemberAGI(mem_id)
    print(row)
    userArr = np.zeros(16)
    age = row[0]
    gender = row[1]
    inter1= row[2]
    if age <20:
        userArr[0] = 1
    elif age >= 20 and age < 30:
        userArr[1] = 1
    elif age >= 30 and age < 40:
        userArr[2] = 1
    elif age >= 40 and age < 50:
        userArr[3] = 1
    elif age >= 50:
        userArr[4] = 1
    if gender == 'M':
        userArr[5] = 1
    elif gender == 'F':
        userArr[6] = 1
    userArr[int(inter1) + 6] = 1
    h5Path = "./ai01/interest.h5"
    book1, book2, book3 = rbDao.recommandBook(userArr,h5Path)
    return book1 +"," + book2 + "," + book3

@app.route('/recommandMBTI', methods=['POST', 'GET']) 
def recommandMBTI():
    dao = MBTI()
    rbDao = AI_Module4()
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "aa"
    row = dao.selectMBTI(mem_id)
    userArr = np.zeros(8)
    a=list(row[2])
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
    h5Path = "./ai04/mbti_book.h5"
    book1, book2, book3 = rbDao.recommandBook(userArr,h5Path)
    return book1 +"," + book2 + "," + book3

@app.route('/recommandMovie', methods=['POST', 'GET']) 
def recommandMovie():
    dao = MOR()
    aidao = AI_Module5()
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "aa"
    row = dao.selectMovieHistory(mem_id)
    genre0 = 0
    genre1 = 0
    genre2 = 0
    genre3 = 0
    genre4 = 0
    genre5 = 0
    for r in row:
        genre = dao.selectMovieGenre(r[0])[0]
        print(genre)
        if genre == 0:
            genre0 += 1
        elif genre == 1:
            genre1 += 1
        elif genre == 2:
            genre2 += 1
        elif genre == 3:
            genre3 += 1
        elif genre == 4:
            genre4 += 1
        elif genre == 5:
            genre5 += 1
    max = 0
    maxVal = 0
    if genre0 > max:
        max = genre0
        maxVal = 0
    elif genre1 > max:
        max = genre0
        maxVal = 1
    elif genre2 > max:
        max = genre1
        maxVal = 2
    elif genre3 > max:
        max = genre2
        maxVal = 3
    elif genre4 > max:
        max = genre3
        maxVal = 4
    elif genre5 > max:
        max = genre4
        maxVal = 5
    if max<2 :
        max = 0
    elif max>=2 and max <5 :
        max = 1
    elif max>=5 :
        max = 2
    userArr =[maxVal,max]
    userArr_n = np.array(userArr)
    userArr_n =userArr_n.reshape((1, 2))
    userArr_n = userArr_n.astype('float32') 
    h5Path = "./ai05/movieAI.h5"
    movie1,movie2,movie3 = aidao.recommandMovie(userArr, h5Path)
    return movie1+","+movie2+","+movie3

@app.route('/recommandReview', methods=['POST', 'GET']) 
def recommandReview():
    dao = MBTI2()
    rbDao = AI_Module6()
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "aa"
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
    h5Path = "./ai06/MBTIMovie.h5"
    movie1, movie2, movie3 = rbDao.recommandMBTIMovie(userArr, h5Path)
    return movie1 +"," + movie2 + "," + movie3

@app.route('/recommandRecord', methods=['POST', 'GET']) 
def recommandRecord():
    kdcDao = getBookNo()
    rbDao = AI_Module2()
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "aa"
    
    row = kdcDao.selectBookNoOfMember(mem_id)
    userArr = row
    print(userArr)
    h5Path = "./ai02/kdcBook.h5"
    book1, book2, book3 = rbDao.recommandBook(userArr,h5Path)
    return book1 +"," + book2 + "," + book3

@app.route('/recommandFace', methods=['POST', 'GET']) 
def recommandFace():
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "Sub"
    npyPath = "./ai03/"+mem_id
    ai_dao = AI_Module3()
    book_dao = celebBook() 
    h5path = "./ai03/celeb.h5"
    celeb = ai_dao.recommandFace(npyPath, h5path)
    
    row = book_dao.selectCelebBook(celeb)
    print(row)
    book1 = str(row[0][0])
    book2 = str(row[1][0])
    book3 = str(row[2][0])
    return book1 +"," + book2 + "," + book3

@app.route('/stupidBook', methods = ['POST', 'GET']) 
def index():
    return render_template('webcam.html')


if __name__ == '__main__':
    app.run(debug=True)
