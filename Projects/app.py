import flask
from flask import request
from flask import render_template
app = flask.Flask(__name__)


from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return '<h1>iClinic </h1>'

#Route  of the main index page
@app.route("/predict",methods=['GET'])
def predict():
    
    from sklearn.externals import joblib
    model = joblib.load('hd_predic.ml')
    predicted = model.predict([[int(request.args['age']), 
                        int(request.args['sex']), 
                        int(request.args['cp']), 
                        int(request.args['trestbps']), 
                        int(request.args['chol']), 
                        int(request.args['fbs']), 
                        int(request.args['restecg']), 
                        int(request.args['thalach']), 
                        int(request.args['exang']), 
                        float(request.args['oldpeak']), 
                        int(request.args['slope']), 
                        int(request.args['ca']), 
                        int(request.args['thal']),
                        ]])
    if predicted == 1:
        a = "Unfortunately there is a possibility of having heart disease"
    else:
            a = "Congratulations!!! There are no any indications of heart disease"
    return str(a)

if __name__ == "__main__":
    app.run(debug=True)

