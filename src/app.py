#!flask/bin/python
from dotenv import load_dotenv
import os

from flask import Flask
from flask import Response

load_dotenv()

app = Flask(__name__)

@app.route('/')
def main():
    
    return Response('OK', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
