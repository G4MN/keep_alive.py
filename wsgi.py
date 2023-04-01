from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

# Define the WSGI application object
wsgi_app = app.wsgi_app
