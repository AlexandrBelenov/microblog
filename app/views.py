from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import flask_microblog, db, lm, oid
from app.forms import LoginForm
from app.models import User, ROLE_USER, ROLE_ADMIN


@flask_microblog.route('/login', methods=["GET", "POST"])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
        title='Sign In',
        form=form,
        providers=flask_microblog.config['OPENID_PROVIDERS'])


@flask_microblog.route('/logout')   
def logout():
    logout_user()
    return redirect(url_for('index'))


def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@flask_microblog.before_request
def before_request():
    g.user = current_user


@flask_microblog.route("/")
@flask_microblog.route("/index")
@login_required
def index():
    current_user = g.user
    posts = [{
            "author": {"nickname": "Ivan"},
            "body": "There are a lot of signs in SPB"
        }, {
            "author": {"nickname": "Obi Wan"},
            "body": "Hello there!"
        }]
    return render_template("index.html", title="Home", user=current_user, posts=posts)
    