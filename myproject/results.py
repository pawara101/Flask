from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    results_dict = {'phy':50,'che':100,'maths':70}
    return render_template('result.html',result=results_dict)

if __name__ == '__main__':
   app.run(debug = True)