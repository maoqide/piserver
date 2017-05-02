from flask import Flask,render_template,request,redirect,url_for
#import motoctl
import motoctl_pwm
app = Flask(__name__)
#moto = motoctl.moto(6, 13, 19, 26)
moto = motoctl_pwm.Moto(6, 13, 19, 26, 21, 20)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/ctl', methods=['POST'])
def control():
    if request.form["direction"] == "forward":
        print "forward"
        moto.forward()				# you can also call the function like 'moto.forward(dc)' to custom duty cycle.(0.0 <= dc <= 100.0, default 50)
        return "car forward"
    elif request.form["direction"] == "backward":
        print "backward"
        moto.backward()				# you can also call the function like 'moto.backward(dc)' to custom duty cycle.(0.0 <= dc <= 100.0, default 50)
        return "car backward"
    elif request.form["direction"] == "left":
        print "left"
        moto.left()				# you can also call the function like 'moto.left(dc)' to custom duty cycle.(0.0 <= dc <= 100.0, default 50)
        return "car left"
    elif request.form["direction"] == "right":
        print "right"
        moto.right()				# you can also call the function like 'moto.right(dc)' to custom duty cycle.(0.0 <= dc <= 100.0, default 50)
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

