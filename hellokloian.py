from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Kloians!'

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
