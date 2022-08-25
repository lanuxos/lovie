# helloFlask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloFlask():
    return 'Hello, Flask'