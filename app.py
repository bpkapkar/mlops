from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

# Load the trained model
clf = joblib.load('trained_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the JSON data from the POST request
        data = request.get_json()
        
        # Extract the input_data from the JSON data
        input_data = data['input_data']
        
        # Perform prediction using the loaded model
        prediction = clf.predict(input_data)
        
        # Convert the prediction to list format
        prediction_list = prediction.tolist()
        
        # Prepare and return the JSON response
        response = {'prediction': prediction_list}
        return jsonify(response)
    
    else:
        return 'This is a GET request'

if __name__ == '__main__':
    app.run()
