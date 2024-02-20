from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Matthew Emaikwu! This is my first HTML page.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()