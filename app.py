
import numpy as np
import pickle
import math

from flask import Flask, jsonify, request 


app = Flask(__name__) 
model = pickle.load(open('final_model_v3.pkl', 'rb'))

@app.route('/')
def home(): 
	
		return jsonify({"message" : "Hi! there"}) 


@app.route('/home/predict', methods = ['POST']) 
def predict():
	
    data = request.get_json(force=True)
    json = list(data.values())
    prediction = model.predict([np.array(json)])

    output = prediction[0]
	dic = {}
	dic["key"] = output
    return jsonify(dic)

 
if __name__ == '__main__': 

	app.run(debug = True)
