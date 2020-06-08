from flask import render_template
from app import flask_microblog


@flask_microblog.route("/")
@flask_microblog.route("/index")
def index():
    current_user = {"nickname": "Alexander"}
    posts = [{
            "author": {"nickname": "Ivan"},
            "body": "There are a lot of signs in SPB"
        }, {
            "author": {"nickname": "Obi Wan"},
            "body": "Hello there!"
        }]
    return render_template("index.html", title="Home", user=current_user, posts=posts)
    