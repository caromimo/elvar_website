#!/usr/bin/env python

import pymongo
from pymongo import Connection
from flask import Flask, render_template, g, request, redirect, url_for
from flask.ext.babel import Babel

app = Flask (__name__)
babel = Babel(app)
connection = Connection('localhost', 27017)
db = connection.elvar
videos = db.videos

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')

@babel.localeselector
def get_locale():
    return g.get('current_lang', 'en')

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        if request.view_args['lang_code'] not in ('en', 'fr'):
            return abort(404)

# the following is Flask's job, i.e. to look up if the url exists. If it
# does, it will carry on the code, here execute the filter function.
# TODO: fix the @app.route("/"):
@app.route("/")
def root():
    return redirect(url_for('default', lang_code='en'))

@app.route("/<lang_code>/")
def default():
    tags = db.videos.distinct("tags")
    tags.sort()
    filtered_videos = videos.find()
    return render_template("index.html", filtered_videos=filtered_videos, current_locale=get_locale())

@app.route("/<lang_code>/filter/<tag>")

# this is our code talking to mongodb inside the filter function
def filter(tag):
    # show the documentaries associated with this tag
    filtered_videos = videos.find({"tags": tag})
    return render_template("index.html", filtered_videos=filtered_videos, current_locale=get_locale())

if __name__ == "__main__":
    app.run(debug=True)
