from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Teste')
def algo():
    return 'Xablau'

if __name__ == '__main__':
    app.run()