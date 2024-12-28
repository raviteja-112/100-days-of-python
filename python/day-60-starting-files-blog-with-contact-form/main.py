from flask import Flask, render_template,request
import requests
import smtplib


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user="example.com",password = "password")
        #     connection.sendmail(from_addr="my_email",to_addrs="abc@gmail.com",msg = "Subject:New Entry\n\n"
        #                         f"name:{data["name"]} email:{data["email"]} phone:{data["phone"]} message:{data["message"]}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

# @app.route("/form-entry",methods = ["POST"])
# def receive_data():
#     data = request.form

#     return "<h1>submitted</h1>"



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
