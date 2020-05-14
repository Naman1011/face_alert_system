import pickle
import numpy as np
from flask import Flask, jsonify, request 


app = Flask(__name__) 
model = pickle.load(open('try02.pkl', 'rb'))

@app.route('/')
def home(): 
	
		return jsonify({"message" : "Hi! there"}) 

@app.route('/home/predict', methods = ['POST']) 
def predict(): 
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__': 

	app.run(debug = True) 
