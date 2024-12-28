from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

login_manager = LoginManager()


app = Flask(__name__)
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'



# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ravi/Documents/computer/python/day-68-starting-files-flask-auth/instance/users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)

class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods = ["POST","GET"])
def register():
    if request.method == "POST":
        user_email = request.form.get('email')
        existing_user = User.query.filter_by(email = user_email).first()
        if existing_user:
            flash("User already exists.Please log in")
            return redirect(url_for('login'))
    
        hash_salt_password = generate_password_hash(
            request.form.get('password'),
            method="pbkdf2:sha256",
            salt_length=8,
        )
        username = request.form.get('name')
        
        new_user = User(
            email=user_email,
            name= username,
            password=hash_salt_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return render_template("secrets.html")
        
    return render_template("register.html")


@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        # Check stored password hash against entered password hashed.
        # if user:
        #     if check_password_hash(user.password, password):
        #         login_user(user)
        #         return redirect(url_for('secrets'))

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():

    return render_template("secrets.html",name = current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static",path="files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)
