from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

URL = "https://api.themoviedb.org/3/search/movie?query="
header = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYTFkZTJiOTFhZDc2MzI1OWNhNGVhNzc3OGE1NDMzNyIsIm5iZiI6MTcyMTQ4ODYzMy4yNjEwODcsInN1YiI6IjY2OWEwOWU5OTAwNTU2ZTY5ZTNhOTBhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ro6gd5uTeeutNTIL21kcexgMMOrT8gummhNFo37Hq7E"
}

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data", "Movies.db"))
# CREATE TABLE
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# initialize the app with the extension
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class Form(FlaskForm):
    rating = StringField('Rating out of 10:')
    review = StringField('Review:') 
    submit = SubmitField(label="Update") 

class addForm(FlaskForm):
    movie = StringField("Movie Title",validators=[DataRequired()])
    submit = SubmitField(label="Add movie")

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )




# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    movie = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = movie.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    return render_template("index.html",movies = all_movies)

@app.route('/update',methods = ["GET","POST"])
def update():
    form = Form()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie,movie_id)
    if request.method == "POST":
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',movie = movie,form = form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    find_url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    data = requests.get(url=find_url,headers = header).json()
    new_movie = Movie(
    title = data["title"],
    img_url = "https://image.tmdb.org/t/p/original/"+f"{data['poster_path']}",
    year = data['release_date'].split("-")[0],
    description = data["overview"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("update",id = new_movie.id))


@app.route("/delete",methods = ["GET","POST"])
def delete():
    movie_id = request.args.get('id')
    movie_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add",methods = ["POST","GET"])
def add():
    addform = addForm()
    if addform.validate_on_submit():
        movie_title = addform.movie.data
        response = requests.get(url = URL+movie_title,headers = header)
        response = response.json()["results"]
        return render_template("select.html",options = response)
    return render_template("add.html",form = addform)

if __name__ == '__main__':
    app.run(debug=True)
