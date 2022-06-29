#!/usr/bin/python
import sys


current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    word,count = line.split('   ',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}   {current_count}")
        current_count = count
        current_word = word
if current_word == word:
    print(f"{current_word}   {current_count}")