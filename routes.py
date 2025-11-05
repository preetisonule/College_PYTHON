from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello user!"

@app.route('/admin')
def admin():
    return "Hello Admin"

@app.route('/home/<name>')
def name(name):
    return "Hello %s"% name

if __name__ == '__main__':
    app.run(debug=True)