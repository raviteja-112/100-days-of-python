from flask import Flask,render_template
import requests
app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7").json()

@app.route("/")
def get_all_posts():
    return render_template("index.html",all_posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/posts/<int:index>")
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post

    return render_template("post.html",post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)