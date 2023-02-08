import flask

app = flask.Flask(__name__)

@app.route('/')
def resume():
    return flask.send_file("resume.pdf")

@app.route("/pdork")
def pdork():
    return flask.redirect("https://pdork.secureighty.me")


app.run()
