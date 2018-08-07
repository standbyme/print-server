
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.headers)
    print(request.form)
    return 'Hi'


app.run(host = '0.0.0.0')
