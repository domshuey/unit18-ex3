"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    def __init__(self, txt):
        '''pull and read txt file, pull a random integer --> index, convert text file to list of tuples (index, word)'''
        file = open(txt, 'r')
        # create tuple list (index, word) from txt file
        self.txt = list((index, word) for index, word in enumerate(file))
        # find length of text file, for end range to randomly generate index
        self.num_lines = len(self.txt)
        file.close()
      

    def random(self):
        '''loop through tuple list, matches indexes and returns word '''

        # random index generation
        self.index = randint(0, self.num_lines)
        for index, word in self.txt:
            if self.index == index:
                # [:-2] to remove /n 
                return word[:-1]
        

    # def find_word(self, word_list):
    #     if self.index in word_list:
