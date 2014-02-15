#!/usr/bin/env python

# this script thumbnails images to a 150x150 thunbnail images with a white
# background and renames each image

import argparse
import glob
from subprocess import call
import os

parser = argparse.ArgumentParser(description='deals with arg')
parser.add_argument('-f', '--folder', help='Enter the folder you want to content to be resized', required=True)

args=parser.parse_args()

file_paths = glob.glob(args.folder+"*")

for file_path in file_paths:
  path, file_name = os.path.split(file_path)
  output_file_name = path + "/resized_" + file_name
  call(["convert", "-resize", "150x150", "-background", "white",
   "-gravity", "center", "-extent", "150x150", file_path,
   output_file_name])
