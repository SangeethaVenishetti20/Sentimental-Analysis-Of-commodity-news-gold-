from flask import Flask, render_template, request,url_for,redirect,session
import pickle
import os
import re
app = Flask(__name__)
# Load your trained model
with open('goldnewsanalysis3.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
@app.route('/')
def home():
    return render_template('minor.html')
@app.route('/predict')
def predict():
    return render_template('predict.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/output', methods=['POST','GET'])
def output():
    if request.method == 'POST':  # Correct way to check if the request method is POST
        newsline = request.form["headline"]
        pred = [newsline]
        output = model.predict(pred)
        print(output)  # For debugging purposes

        # Determine the output message based on the prediction
        if output[0] == 'positive':
            output_msg = 'Upward movement in gold price'
        elif output[0] == 'negative':
            output_msg = 'Downward movement in gold price'
        elif output[0] == 'neutral':
            output_msg = 'Steady movement in gold price'
        elif output[0] == 'none':
            output_msg = 'This news headline is not related to gold news'
        else:
            output_msg = 'Prediction not found'

        return render_template('output.html', output=output_msg)

    # If GET request or no prediction made, render the template without output message
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)