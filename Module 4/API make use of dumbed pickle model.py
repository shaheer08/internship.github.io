import numpy as np 
from flask import flask, abort, jsonify, request
import cpickle as pickle

my_random_forest = pickle.load(open("iris_rfc.pkl", "rb"))
app = Flask(_name_)

@app.route('/predict',methods=['POST'])
def make_predict():
	data = request.get_json(force=True)
	predict_request = [data['sl'],data['sw'],data['pl'],['pw']]
	predict_request = np.array(predict_request)
	y_hat = my_random_forest.predict(predict_request)
	output = [y_hat[0]]
	return jsonify(results=output)

	if __name__ == '__main__':
    app.run(debug=True, port=port)