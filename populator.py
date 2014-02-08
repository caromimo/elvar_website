#!/usr/bin/env python

import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

# the following indicates which database and collection to interact with:
db = connection.elvar
videos = db.videos

# then we need to establish a connection between yaml (which holds the
# raw data) and mongodb (which will hold the data in a searchable way)

# yaml will be used to parse a text file
import yaml
# open a text file (.yml) and read it
content = open("videos.yml").read()
# parse the content of the opened text file
parsed_content = yaml.load(content)
# insert the parsed content to a mondodb
for video in parsed_content:
    videos.save(video)
