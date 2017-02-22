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

sum_to_output = 0
previouseChannelTV = None

file = open('submit', 'w+')
with open('out') as f:
    content = f.readlines()
    for line in content:
        line       = line.strip()       #strip out carriage return
        key_value  = line.split('\t')   #split line, into key and value, returns a list

        #note: for simple debugging use print statements, ie:
        curr_TV  = key_value[0]         #key is first item in list, indexed by 0
        value_in   = key_value[1]         #value is 2nd item

        # sum all TV channels up
        if(curr_TV == previouseChannelTV or previouseChannelTV == None):
            previouseChannelTV = curr_TV
            sum_to_output = sum_to_output + int(value_in)
        else:
            previouseChannelTV = None
            file.write('%s\t%s\n' % (curr_TV, sum_to_output))
            sum_to_output = 0
            #print('%s\t%s' % (curr_TV, value_in))

