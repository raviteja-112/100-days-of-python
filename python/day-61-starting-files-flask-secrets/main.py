from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    email = StringField(label='name',validators=[DataRequired(),Email()])
    # password = StringField('password')
    password = PasswordField(label='password',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="log in")


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "fruit juice"
emails = ["admin@email.com"]
passwords = ["12345678"]
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods = ['POST','GET'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data in emails and login_form.password.data in passwords:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html",form = login_form)

if __name__ == '__main__':
    app.run(debug=True)
