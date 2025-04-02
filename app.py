import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/resume')
def resume():
    return flask.send_file("Taylor_Aedan_AT_Resume.pdf")

@app.route('/blog')
def blog():
    return flask.redirect(https://secureighty.me/blog/)

@app.route('/rickroll')
def rickroll():
    return flask.redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.route("/pdork")
def pdork():
    return flask.redirect("https://pdork.secureighty.me")

@app.route("/palo")
def palo():
    return flask.redirect("https://paloaltonetworks.responsibledisclosure.com/hc/en-us/articles/360037368173")

@app.route("/cheshire_tree")
@app.route("/cheshiretree")
@app.route("/ct")
def cheshire_tree():
    return flask.redirect("https://www.dropbox.com/scl/fo/6jkphbszif6nkpzrsw62f/h?rlkey=6i0tbn6t3xf4ag961050sa55d&dl=0")

app.run()
