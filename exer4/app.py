from flask import Flask, render_template,request, url_for, redirect
app = Flask(__name__)

@app.route("/user")
def user():
    pass
    # return render_template('xxxx')

@app.route('/hello/', methods=['POST'])
def hello():
	allowed_list = ["larry", "leijun","boss"]
	print request.form
	name = "<TODO>"
	# return redirect(....)
	# if name in allowed_list:
	# else:
	
@app.route("/user/<name>")
def hello_user(name):
	return render_template('hello.html',name=name)
	
@app.route("/")
def home():
	return redirect(url_for('user'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
