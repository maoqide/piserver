from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/ctl', methods=['POST'])
def control():
    if request.form["direction"] == "forward":
        print "forward"
        return "car forward"
    elif request.form["direction"] == "backward":
        print "backward"
        return "car backward"
    elif request.form["direction"] == "left":
        print "left"
        return "car left"
    elif request.form["direction"] == "right":
        print "right"
        return "car right"
    elif request.form["direction"] == "stop":
        print "stop"
        return "car stop"

    print "hello"
    return redirect(url_for('index'))
#    return "hello"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

