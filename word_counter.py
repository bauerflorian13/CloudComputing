#!/usr/bin/env python3

from collections import Counter
import nltk
import sys

if len(sys.argv) != 2:
    print("The argument musst be the full path of the inputfile.")
    sys.exit(1)

# read the input file
path = sys.argv[1]
f = open(path, 'r')

Text = f.read()

# Cleaning text and lower casing all words
for char in '-.,\n':
    Text=Text.replace(char,' ')
Text = Text.lower()

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
text = Text.split()

# tag all words
pos = nltk.pos_tag(text)

# filter the nouns
word_list = [x for (x,y) in pos if y == 'NN']

# sort the word list
most_common = Counter(word_list).most_common()

# print the most common word list
print("The most common words: \n{}".format(most_common))
