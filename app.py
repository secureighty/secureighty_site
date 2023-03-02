import flask

app = flask.Flask(__name__)

@app.route('/')
def resume():
    return flask.send_file("Taylor_Aedan_AT_Resume.pdf")

@app.route("/pdork")
def pdork():
    return flask.redirect("https://pdork.secureighty.me")

@app.route("/palo")
def palo():
    return flask.redirect("https://paloaltonetworks.responsibledisclosure.com/hc/en-us/articles/360037368173")


app.run()
