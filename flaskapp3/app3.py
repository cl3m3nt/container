from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_page():
    return 'Welcome my ML Model application'

@app.route('/model1/<int:input>')
def mlmodel1(input):
    return 'Prediction %d from ML model1' %input

@app.route('/model2/<int:input>')
def mlmodel2(input):
    return 'Prediction %d from ML model2' %input

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')