#!/usr/bin/python3

# Micmath2016

# Permet de trouver les mots dont le produit des lettres est égal à 2016
# et aux autres années passées.

# Auteur : Nathanaël Jourdane
# Email: nathanael@jourdane.net
# Date : 1er janvier 2016
# License: Creative Commons CC-BY (Attribution)

# La vidéo de de Micmath proposant le défi :
# https://www.youtube.com/watch?v=lrcXq3Bd474

# La liste des mots de la langue française :
# http://www.pallier.org/ressources/dicofr/dicofr.html

# Pour 2016, il y a donc 6 mots:
# - chaud : 3 * 8 * 1 * 21 * 4 = 2016
# - flagada : 6 * 12 * 1 * 7 * 1 * 4 * 1 = 2016
# - pain : 16 * 1 * 9 * 14 = 2016
# - panai : 16 * 1 * 14 * 1 * 9 = 2016
# - pian : 16 * 9 * 1 * 14 = 2016
# - pin : 16 * 9 * 14 = 2016

import unicodedata, string

years = {}
with open('./mots', 'r') as infile:
	for word in infile:
		prod=1
		formated_word = ''.join(x for x in unicodedata.normalize('NFKD', word) if x in string.ascii_letters).lower()
		detail=''
		for l in formated_word:
			prod *= ord(l)-96
			detail += ' * ' + str(ord(l)-96)

		for year in reversed(range(2016+1)):
			if (prod == year):
				details = word.strip() + ' : ' + detail[3:] + ' = ' + str(year)
				if year in years:
					years[year].append(details)
				else:
					years[year] = [details]

with open('./years', 'w') as outfile:
	for year, words in reversed(sorted(years.items())):
		outfile.write('\n*** ' + str(year) + ' ***\n')
		for word in words:
			outfile.write(word + '\n')