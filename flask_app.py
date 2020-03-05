
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello da Dani!'

@app.route('/inicio')
def inicio():
    return render_template('index.html')


