from flask import Flask, render_template, request, abort
from epidemic import Predict_Epidemic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def predict_epidemic():
    if request.args.get('form'):

        if int(request.args.get('year')) < 0:
             abort(400)

        if request.args.get('form') == 'predict':
            correct, prediction, virus = Predict_Epidemic(int(request.args.get('year')))
            if virus is not None:
                return render_template('1.html', predict_message=f'In {request.args.get("year")}, {virus} happened.', prediction=prediction)
            if prediction == 0:
                return render_template('1.html', predict_message=f'There is {correct * 100}% that an epidemic will not happen in {request.args.get("year")}', prediction=prediction)
            else:
                return render_template('1.html', predict_message=f'There is {correct * 100}% that an epidemic will happen in {request.args.get("year")}', prediction=prediction)


    return render_template('1.html')