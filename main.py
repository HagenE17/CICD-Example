# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # A simple greeting
    return "Hello, DevOps Students! Version 3.0"