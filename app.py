import flask

app = flask.Flask(__name__)

@app.route('/')
def resume():
    return flask.send_file("Taylor_Aedan_AT_Resume.pdf.pdf")

@app.route('/rickroll')
def rickroll():
    return flask.redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.route("/pdork")
def pdork():
    return flask.redirect("https://pdork.secureighty.me")

@app.route("/palo")
def palo():
    return flask.redirect("https://paloaltonetworks.responsibledisclosure.com/hc/en-us/articles/360037368173")


app.run()
