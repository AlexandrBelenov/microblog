from app import flask_microblog


@flask_microblog.route("/")
@flask_microblog.route("/index")
def index():
    return "Hello, world!"