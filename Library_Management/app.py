from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return json.dumps({'Name': "Utsho", 'Age': "21"})

if __name__ == '__main__':
    app.run()
