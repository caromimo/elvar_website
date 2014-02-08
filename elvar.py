#!/usr/bin/env python

import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

from flask import Flask
from flask import render_template

app = Flask (__name__)

db = connection.elvar
videos = db.videos

# the following is Flask's job, i.e. to look up if the url exists. If it
# does, it will carry on the code, here execute the filter function.
# TODO: fix the @app.route("/"):
@app.route("/")
def all_videos():
    tags = db.videos.distinct("tags")
    tags.sort()
    filtered_videos = videos.find()
    return render_template("index.html", filtered_videos=filtered_videos, tags=tags)

@app.route("/filter/<tag>")

# this is our code talking to mongodb inside the filter function
def filter(tag):
    # show the documentaries associated with this tag
    tags = db.videos.distinct("tags")
    tags.sort()
    filtered_videos = videos.find({"tags": tag})
    return render_template("index.html", filtered_videos=filtered_videos, tags=tags)

if __name__ == "__main__":
    app.run(debug=True)
