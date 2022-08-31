from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify


app = Flask(__name__,static_url_path='')


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/')
@app.route('/omok')
def omok():
    return render_template('omok4_20_teacher_ai.html')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
    
    
    
    
    
    
    
    