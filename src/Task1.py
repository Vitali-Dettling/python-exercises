#!/usr/bin/python

# External
import csv
import urllib.request as down

# Manual
import src.utility as utility


url = 'http://www.calvin.edu/~stob/data/Berkeley.csv'

local_filename, headers = down.urlretrieve(url)
cr = csv.reader(local_filename)

utility.display_table(local_filename)