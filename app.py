from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello_world!\n'

@app.route('/hello/')
def hello_hello_world():
    return 'Hello Hello World!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Why Hello %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
