from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
from flask_cors import CORS
from day19_omok_s.aao_omok import AaoOmok


app = Flask(__name__,static_url_path='')
CORS(app)
ao = AaoOmok()

@app.route('/')
def test():
    return render_template('test.html')


@app.route('/ajax', methods=['POST'])
def ajaxmod():
    stone = request.form['stone']
    data400 = request.form['data400']
    print("stone",stone)
    print("data400",data400)
    flagWb = True
    
    arr2D = []
    for i in range(20):
        line = []
        for j in range(20):
            mystr = data400[20*i+j:20*i+j+1]
            myint = int(mystr)
            line.append(myint)
        arr2D.append(line)
        
    if stone =="1":
        flagWb = True
    elif stone =="2":
        flagWb = False 
    
    
    i,j = ao.mypredict(arr2D,flagWb)
    print(i,j);
    
    return jsonify({'i':str(i),'j':str(j)})

if __name__ == '__main__':
    app.run(debug=True,port=5001,host="0.0.0.0")
    
    
    
    

