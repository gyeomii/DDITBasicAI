from flask import Flask, request
import tensorflow as tf
import numpy as np
from flask.json import jsonify
from ai03.ai_module import AI_Module3

app = Flask(__name__)


@app.route('/recommandFace', methods=['POST', 'GET']) 
def recommandFace():
    mem_id = request.args.get('mem_id')
    if mem_id == None:
        mem_id = "Sub"
    
    dao = AI_Module3()
    h5path = "celeb.h5"
    celeb = dao.recommandFace(mem_id, h5path)
    return celeb
        
if __name__ == '__main__':
    app.run(debug=True)
