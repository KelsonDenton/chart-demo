from flask import Flask, jsonify, render_template

app = Flask(__name__)   # __name__ is a DUNDER (double under, look up)
app.config['FLASK_ENV']='development'
app.config['DEBUG']=True

@app.route('/')
def index():
    return "<a href='/chart'>Open Chart</a>"

@app.route('/chart')
def chart_demo():
    return render_template('chart.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', use_reloader=True, debug=True)
