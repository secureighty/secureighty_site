import flask

app = flask.Flask(__name__)

@app.route('/')
def resume():
    return flask.send_file("Taylor_AedanAT_Resume_Feb_2023_2.1.pdf")

app.run("0.0.0.0")