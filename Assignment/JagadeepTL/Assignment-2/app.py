from ast import Not
from itertools import count
from pickle import NONE
import profile
from flask import Flask, flash,render_template,redirect,request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate


app= Flask(__name__)


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\IBMproject\Assesments\JagadeepTL\Assignment-2\site.db'
app.secret_key = 'the random string'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

 
# Settings for migrations
migrate = Migrate(app, db)

 
# Models
class Profile(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(20), nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.u_name}, email: {self.email}"

@app.route('/')
def ex():
    return render_template('login.html')



@app.route('/show_db')
def index():
	# Query all data and then pass it to the template
	profiles = Profile.query.all()
	return render_template('show_db_data.html', profiles=profiles)


@app.route('/add_data',methods=['POST','GET'])
def add_data():
    uname = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password") 
 
    # create an object of the Profile class of models
    # and store data as a row in our datatable
    user = Profile.query.filter_by(u_name=uname).first()
    if user is None:
      if uname != '' and email != '' and password is not None:
        p = Profile(u_name=uname, email=email, password=password)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
      else:
        return redirect('/')
    else:
        flash('Username Already Exist')
        return redirect('/signup')



@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/loginValidate',methods=['GET','POST'])
def loginvalid():
    uname=request.form.get("username")
    password=request.form.get("password")
    user = Profile.query.filter_by(u_name=uname,password=password).first()
    if  user is NONE :
        flash("Invalid Credentials")
        return redirect('/')
    else:
        return render_template('home.html')



        


if __name__ =='__main__':
  app.run(debug=True)
