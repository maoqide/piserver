from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template("hello.html", name=name)

@app.route('/ctl', methods=['POST'])
def control():
    if request.form["direction"] == "forward":
	    return "car forward"
    return 'control the car'

