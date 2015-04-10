# We need 'datetime' module for getting the current time
# We need the 're' module to validate email address using regular expressions
# We import 'Flask' to create an app,
# 'request' to access the request data in each view
# 'flash' to send messages to be displayed in the template
# 'url_for' to get the URL for a given view function name
# 'redirect' to redirect to a given URL
# 'render_template' to render a template
# 'flask_sqlalchemy' provides a wrapper over SQLAlchemy. Install
# 'flask-sqlalchemy' package to use this.

from datetime import datetime
import re
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

# Creates a Flask app and reads the settings from a 
# configuration file. We then connect to the database specified
# in the settings file
app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)


# We are defining a 'Comments' model to store the comments the user
# enters via the form.
class Comments(db.Model):
  # Setting the table name and
  # creating columns for various fields
  __tablename__ = 'comments' 
  id = db.Column('comment_id', db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  comment = db.Column(db.String(200))
  pub_date = db.Column(db.DateTime)
  
  def __init__(self, name, email, comment):
      # Initializes the fields with entered data
      # and sets the published date to the current time
      self.name = name
      self.email = email
      self.comment = comment
      self.pub_date = datetime.now()


def is_email_address_valid(email):
  """Validate email address using regular expression."""
  if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
      return False
  return True


# The default route for the app. 
# Displays the list of already entered comments
# We are getting all the comments ordered in 
# descending order of pub_date and passing to the
# template via 'comments' variable
@app.route('/')
def show_all():
  return render_template('show_all.html', comments=Comments.query.order_by(Comments.pub_date.desc()).all()  )

# Create tale
@app.route('/create')
def create():
  db.create_all(app=app)
  return redirect(url_for('show_all'))
  
# Create tale
@app.route('/drop')
def drop():
  db.drop_all(app=app)
  return redirect(url_for("create")) 

# This view method responds to the URL /new for the methods GET and POST
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # The request is POST with some data, get POST data and validate it.
        # The form data is available in request.form dictionary.
        # Check if all the fields are entered. If not, raise an error
        if not request.form['name'] or not request.form['email'] or not request.form['comment']:
            flash('Please enter all the fields', 'error')
            
        # Check if the email address is valid. If not, raise an error
        elif not is_email_address_valid(request.form['email']):
            flash('Please enter a valid email address', 'error')
        
        else:
            # The data is valid. So create a new 'Comments' object
            # to save to the database
            comment = Comments(request.form['name'],
                               request.form['email'],
                               request.form['comment'])
    
            # Add it to the SQLAlchemy session and commit it to
            # save it to the database
            
            db.session.add(comment)
            db.session.commit()
            
            # Flash a success message
            flash('Comment was successfully submitted')
            
            # Redirect to the view showing all the comments
            return redirect(url_for('show_all'))
    
    # Render the form template if the request is a GET request or
    # the form validation failed
    return render_template('new.html')


# This is the code that gets executed when the current python file is
# executed. 
if __name__ == '__main__':
  # Run the app on all available interfaces on port 80 which is the
  # standard port for HTTP
	app.run(host="0.0.0.0")
 