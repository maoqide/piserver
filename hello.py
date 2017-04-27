from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template("hello.html", name=name)

@app.route('/ctl', methods=['POST'])
def control():
    return 'control the car'

@app.route('/test', methods=['GET','POST'])
def test():
    print "----------------------start request------------------------"
    print "form: ", request.form
    print "args: ", request.args
    print "values: ", request.values
    print "cookies: ", request.cookies
    print "stream: ", request.stream
    print "headers: ", request.headers
    print "data: ", request.data
    print "files: ", request.files
    print "environ: ", request.environ
    print "method: ", request.method
    print "path: ", request.path
    print "script_root: ", request.script_root
    print "url: ", request.url
    print "base_url: ", request.base_url
    print "url_root: ", request.url_root
    print "is_xhr: ", request.is_xhr
    print "blueprint: ", request.blueprint
    print "endpoint: ", request.endpoint
    print "get_json: ", request.get_json(force=False, silent=False, cache=True)
    print "json: ", request.json
    print "max_content_length: ", request.max_content_length
    print "module: ", request.module
    print "routing_exception: ", request.routing_exception
    print "url_rule: ", request.url_rule 
    print "view_args: ", request.view_args
    print "----------------------end request--------------------------"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
