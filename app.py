from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
        retorn "Hello, World!"

if __name__ == '__main':
        app.run(host='0.0.0.0', port=8080)