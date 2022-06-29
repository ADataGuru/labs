#!/usr/bin/python
import sys

# input comes from standard input STDIN

for line in sys.stdin:
    words = line.split(" ") # Créer une liste de mots à partir du séparateur " "
    ip = words[0] # Retrouver la position de l'ip
    # Ecrire le résultat sur la sortie standard (stdout)
    output = f"{ip}   1"
    print(output)

