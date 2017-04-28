from flask import Flask,render_template,request,redirect,url_for
import motoctl
app = Flask(__name__)
moto = motoctl.moto(6, 13, 19, 26)
@app.route('/')
def index():
    return render_template("main.html")

@app.route('/ctl', methods=['POST'])
def control():
    if request.form["direction"] == "forward":
        print "forward"
        moto.forward()
        return "car forward"
    elif request.form["direction"] == "backward":
        print "backward"
        moto.backward()
        return "car backward"
    elif request.form["direction"] == "left":
        print "left"
        moto.left()
        return "car left"
    elif request.form["direction"] == "right":
        print "right"
        moto.right()
        return "car right"
    elif request.form["direction"] == "stop":
        print "stop"
        moto.stop()
        return "car stop"
    else:
        print "hello"
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=15000)

