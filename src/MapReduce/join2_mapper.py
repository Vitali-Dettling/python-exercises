#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into
#  the value field for output
#
#  Note, this program is written in a simple style and does not full advantage of Python
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------

EOF = []
channelTVs = []

file = open('Data/out', 'w+')
with open('Data/in') as f:
    content = f.readlines()
    for line in content:

        line       = line.strip()   #strip out carriage return
        key_value  = line.split(",")#split line, into key and value, returns a list
        key_in     = key_value[0]   #key is first item in list
        value_in   = key_value[1]   #value is 2nd item

        if value_in == 'ABC' or value_in.isdigit():
            EOF += ['{0}\t{1}\n'.format(key_in, value_in)]

    sort = sorted(EOF, reverse=True)
    for i in range(0, len(sort)-1):
        file.write(sort[i])


#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value