from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
class Form(FlaskForm):
    rating = StringField('Potential')
    review = StringField('Time') 
    submit = SubmitField(label="Update") 

@app.route("/")
def hello_world():
    form = Form()
    return render_template("home.html",form = form)


if __name__ == "__main__":
    app.run(debug=True)
