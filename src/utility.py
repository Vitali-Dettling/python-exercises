#!/usr/bin/python

import csv

def display_table( local_filename ):
   with open(local_filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)