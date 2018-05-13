# server.py
from os import environ, path
from flask import Flask, render_template, send_from_directory


here = path.abspath(path.dirname(__file__))
print(here)

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/")
def index():
    message = 'This is from da python'
    return render_template("index.html", message=message)

@app.route("/hello")
def hello():
    return "Hello World Bobbo bobobob!"

@app.route("/images/<path:filename>")
def send_asset(filename):
    return send_from_directory(path.join(here, "../static/images"), filename)

if __name__ == "__main__":
    app.run()