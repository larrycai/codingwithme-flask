from flask import Flask, render_template
app = Flask(__name__)

@app.route("/user")
def user():
    return "<p>Please use <a href='http://192.168.59.103:5000/user/larry'>http://192.168.59.103:5000/user/larry</a> ( or other /user/<id> ) instead "

@app.route("/user/<name>")
def hello_user(name):
    return "Hello %s!" % name
    # render_template(....)
	
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
