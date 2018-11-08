#!/usr/bin/env python3

from collections import Counter
import nltk

# TODO: Add test input reader
Text = """
bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.  We hold these truths to be
self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness
"""

# Cleaning text and lower casing all words
for char in '-.,\n':
    Text=Text.replace(char,' ')
Text = Text.lower()

# just filter the nouns
#text = word_tokenize(Text)
text = Text.split()
pos = nltk.pos_tag(text)

word_list = [x for (x,y) in pos if y == 'NN']


# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
#word_list = Text.split()

most_common = Counter(word_list).most_common()

print(word_list)

print(most_common)
