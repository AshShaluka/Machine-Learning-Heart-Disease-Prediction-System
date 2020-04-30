import flask
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

#Route  of the main index page
@app.route('/')
def home():
    return '<h1>working</h1>'

#Route of the predict page
@app.route('/predict')
def predict():
    from sklearn.externals import joblib
    
    model = joblib.load('hd_predic.ml')
    hd_predic = model.predict([[request.args['age'], 
                        request.args['sex'], 
                        request.args['cp'], 
                        request.args['trestbps'], 
                        request.args['chol'], 
                        request.args['fbs'], 
                        request.args['restecg'], 
                        request.args['thalach'], 
                        request.args['exang'], 
                        request.args['oldpeak'], 
                        request.args['slope'], 
                        request.args['ca'], 
                        request.args['thal']]])
    return str(hd_predic)



app.run(debug=True)