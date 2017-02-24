#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

channels = []
joinedChannels = {}
sum_to_output = 0
previousChannel = None

file = open('Data/submit', 'w+')
with open('Data/out') as f:
    content = f.readlines()
    for line in content:
        line       = line.strip()       #strip out carriage return
        key_value  = line.split('\t')   #split line, into key and value, returns a list

        key_in  = key_value[0]         #key is first item in list, indexed by 0
        value_in   = key_value[1]         #value is 2nd item

        # sum all TV channels up
        if(value_in == 'ABC'):
            channels = [key_in]

        if(value_in.isdigit() and key_in in channels):
            if(previousChannel == key_in):
                joinedChannels[key_in] = int(joinedChannels[key_in]) + int(value_in)
            else:
                previousChannel = key_in
                joinedChannels[key_in] = value_in

for key, value in joinedChannels.iteritems():
    file.write('%s\t%s\n' % (key, value))


