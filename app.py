import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle      # to load the model we have saved

app = Flask(__name__)  # creating flask app
model= pickle.load(open("model.pkl","rb"))

@app.route('/')   # / represent the root page
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])  # / predict will hit the function we have created 
# after home this will get executed therefore POST used
def predict():
    # to render results on html gui
    features = [int(x) for x in request.form.values()]  # takes input from all the form we have created 
#in our index.html file
    final_features = [np.array(features)]
    pred = model.predict(final_features)
    
    output = round(pred[0],2)
    
    return render_template('index.html',prediction_text="Employee Salary Should be Rs.{}".format(output))

if __name__ =="__main__":
    app.run(debug=True)