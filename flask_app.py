from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("titanic_model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from JSON request
        data = request.get_json()
        
        # Convert data to DataFrame with an index
        data_df = pd.DataFrame.from_dict(data, orient='index').T

        # Make predictions
        predictions = model.predict(data_df)

        # Return predictions as JSON response
        response = {"predictions": predictions.tolist()}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
    app.run(debug=True)
