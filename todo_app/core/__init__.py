from flask import Flask, render_template


from flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

from core import todo

@app.route('/')
def index():
    return render_template("index.html")