#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):
  tupleList = count_words(filename)
  tupleList.sort(key=tupleValue)
  print_output(tupleList)
  return 1

def print_top(filename):
  tupleList = count_words(filename)
  tupleList.sort(key=tupleCount, reverse=True)
  print_output(tupleList[0:20])
  return 1

def print_output(tupleList):
  for tuple in tupleList:
    print(tupleValue(tuple), " ", tupleCount(tuple))
  return 1

def count_words(filename):
  #The wordList and countList will keep corresponding positioning
  #this uses more memory but searches are quicker
  wordList = list()
  countList = list()
  textfile = open(filename, 'r')
  #Start by reading the first set of lines from filename
  lines = textfile.readlines(100)
  #While there are still lines to read
  while lines:
    #process one line at a time
    for line in lines:
      #the instructions say everything should be treated as lowercase
      #process each word in the line, where words the line delimited by spaces
      for word in line.lower().split(" "):
        #IF we find word in wordList then increment THEN count in countList
        #  the wordList and countList will keep corresponding positioning
        try:
          wordIndex = wordList.index(word)
          countList[wordIndex] = countList[wordIndex] + 1
        except ValueError:
        #ELSE append the word to the wordList, and append a new count to countList
        #  the wordList and countList will keep corresponding positioning
          wordList.append(word)
          countList.append(1)
    # read in the next set of lines (if available) and go back to the while loop test
    lines = textfile.readlines(100)
  textfile.close()
  # return the wordList and countList transposed into a tuple list
  return [[repr(wordList[tupleIndex]), countList[tupleIndex]] for tupleIndex in range(len(wordList))]

def tupleCount(tuple):
  return tuple[1]

def tupleValue(tuple):
  return tuple[0]

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
