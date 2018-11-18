from collections import Counter
import nltk
import sys

class Wordcounter(object):
    def count_words(self, Text):
        # Cleaning text and lower casing all words
        for char in '-.,\n':
            Text=Text.replace(char,' ')
        Text = Text.lower()

        nltk.download('averaged_perceptron_tagger')
        # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
        text = Text.split()

        # tag all words
        pos = nltk.pos_tag(text)

        # filter the nouns
        word_list = [x for (x,y) in pos if y == 'NN']

        # sort the word list
        most_common = Counter(word_list).most_common()

        # print the most common word list
        #print("The most common words: \n{}".format(most_common))
        top3 = most_common[:3]
        top3 = [a for (a,b) in top3]
        return top3