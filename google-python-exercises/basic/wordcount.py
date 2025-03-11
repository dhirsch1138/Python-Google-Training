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
  list = count_words(filename)
  list.sort(key=tupleValue)
  print_output(list)
  return 1

def print_top(filename):
  list = count_words(filename)
  list.sort(key=tupleCount, reverse=True)
  print_output(list[0:20])
  return 1

def print_output(tupleList):
  for tuple in tupleList:
    print(repr(tupleValue(tuple)), " ", tupleCount(tuple))
  return 1

def count_words(filename):
  wordList = list()
  f = open(filename, 'r')
  with f as x:
    line = x.readline().lower()
    while line:
        for y in line.split(" "):
          wordList = logWord(y,wordList)    
        line = x.readline().lower()
  f.close()
  return wordList

def logWord(word, tupleList):
  valueList = listWords(tupleList)
  try:
    x = valueList.index(word)
    tupleList[x] = [word, (tupleCount(tupleList[x]) + 1)]
  except ValueError:
    tupleList = tupleList + [[word, 1]]
  return tupleList

def listWords(tupleList):
  words = list()
  for x in tupleList:
    words = words + [tupleValue(x)]
  return words

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
