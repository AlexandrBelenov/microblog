from flask import render_template, flash, redirect
from app import flask_microblog
from app.forms import LoginForm


@flask_microblog.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for OpenID='{}', remember me= {}".format(form.openid.data, str(form.remember_me.data)))
        return redirect("/index")
    return render_template("login.html",
        title="Sign In",
        form=form,
        providers=flask_microblog.config['OPENID_PROVIDERS'])


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
    