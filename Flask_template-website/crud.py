from flask import *
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abc.sqlite3'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ab.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
db = SQLAlchemy(app)  

class abc(db.Model):
    id =db.Column('abc',db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    phone_no=db.Column(db.String(14))
    email=db.Column(db.String(100))
    message=db.Column(db.String(500))

    def __init__(self, name, phone_no,email,message):  
      self.name=name
      self.phone_no=phone_no
      self.email=email
      self.message =message

class ab(db.Model):
    id =db.Column('abc',db.Integer,primary_key=True)
    email=db.Column(db.String(100))
    phone=db.Column(db.String(13))

    def __init__(self,email,phone):  
      self.email=email
      self.phone=phone

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/action",methods=['GET','POST'])
def action():
    if request.method=='POST':
        if not request.form['name'] or not request.form['phone_no'] or not request.form['email'] or not request.form['message']:
            flash("Please Enter all fields")
        else:
            contact=abc(request.form['name'],request.form['phone_no'],request.form['email'],request.form['message'])
            db.create_all()
            db.session.add(contact)
            db.session.commit()
            flash("Your Data Has Been Saved")
            return redirect(url_for("index"))
        return render_template("index.html")

@app.route("/subscribe",methods=['GET','POST'])
def subscribe():
    if request.method=='POST':
        if not request.form['email'] or not request.form['phone']:
            flash("Please Enter all fields")
        else:
            contacts=ab(request.form['email'],request.form['phone'])
            db.create_all()
            db.session.add(contacts)
            db.session.commit()
            flash("Your Data Has Been Saved")
            return redirect(url_for("index"))
        return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/client')
def client():
    return render_template("client.html")

if __name__ == '__main__':  
   db.create_all()
   app.run(debug = True,port=2000)  
   