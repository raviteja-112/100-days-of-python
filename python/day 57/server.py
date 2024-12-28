from flask import Flask,render_template
import requests
app = Flask(__name__)

URL_GENDER = "https://api.genderize.io/?"
URL_AGE = "https://api.agify.io/?"

@app.route("/guess/<username>")
def guess_age(username):
    parameters = {
        "name":username
    }
    response_gender = requests.get(url=URL_GENDER,params=parameters)
    response_gender.raise_for_status()
    gender_data = response_gender.json()
    response_age = requests.get(url=URL_AGE,params=parameters)
    response_age.raise_for_status()
    age_data = response_age.json()
    
    gender = gender_data["gender"]
    age = age_data["age"]


    
    return render_template("index.html",gender = gender,age = age,name = username.title())



@app.route("/blog")
def blog():
    response_blog = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response_blog.json()

    return render_template("blog.html",blogs = all_blogs)
if __name__ == "__main__":
    app.run(debug=True)