from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/user")
def user():
    return "<p>Please use type xxx "

@app.route("/users")
def users():
    pass
    # return redirect(...)

@app.route("/user/<name>")
def hello_user(name):
    return "Hello %s!" % name
    # if name != xxx :
    #    return ...
    # else:
    # ...
	
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
