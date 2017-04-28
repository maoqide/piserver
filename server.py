from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template("hello.html", name=name)

@app.route('/ctl', methods=['POST'])
def control():
    if request.form["direction"] == "forward":
	    return "car forward"

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

