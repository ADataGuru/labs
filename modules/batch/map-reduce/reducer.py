#!/usr/bin/python
import sys


current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    word,count = line.split('   ') # extraire le mot et le count en variables
    try:
        count = int(count) # Caster le compteur en integer
    except ValueError:
        continue
    if current_word == word:   # Si le mot courant est égal au mot extrait
        current_count += count # On incrémente les compteurs pour le mot
    else:
        if current_word: # Sinon si le mot n'est pas undefined
            print(f"{current_word}   {current_count}")
        current_count = count
        current_word = word
if current_word == word:
    print(f"{current_word}   {current_count}")