from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world():
   return '<h1>hello Pawara</h1>'


if __name__ == '__main__':
   app.run(debug = True)