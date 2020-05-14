
import numpy as np
import pickle
import math

from flask import Flask, jsonify, request 


app = Flask(__name__) 
model = pickle.load(open('test_modelv5.2.pkl', 'rb'))

@app.route('/')
def home(): 
	
		return jsonify({"message" : "Hi! there"}) 


@app.route('/home/predict', methods = ['POST']) 
def predict():
	
    data = request.get_json(force=True)
	  json = list(data.values())
 	  pitch = 180 *math.atan2(json[0], math.sqrt(json[1]*json[1]+ json[2]*json[2]))/math.pi
	  roll = 180 * math.atan2(json[1], math.sqrt(json[0]*json[0] + json[2]*json[2]))/math.pi
	  json.append(pitch)
	  json.append(roll)
    prediction = model.predict([np.array(json)])

    output = prediction[0]
    return jsonify(output)

 
if __name__ == '__main__': 

	app.run(debug = True)
