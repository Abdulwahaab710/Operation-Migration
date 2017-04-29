from birdWatchers import app
from flask import render_template


@app.route('/')
def main():
    return '<h1>hello world!</h1>'
