from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib
import traceback

app = Flask(__name__)

model_name = 'model/iris_rfc.pkl'


@app.route('/predict', methods=['POST'])
def predict():
    if clf:
        try:
            json_ = request.json
            query = pd.DataFrame(json_)

            prediction = (clf.predict(query))
            prediction_values = []

            for items in prediction:
                prediction_values.append(int(items))

            print(prediction)
            return jsonify({'prediction': list(prediction_values)})

        except Exception as e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})

    else:
        print('need to train first')
        return 'no model here'

if __name__ == '__main__':

    clf = None

    try:
        clf = joblib.load(model_name)
        print('Model Loaded')

    except Exception as e:
        print('No model here')
        print('Train First')
        print(str(e))
        clf = None

    app.run(host='127.0.0.1', port=port, debug=True)