#!/usr/bin/python2

import fileinput
from operator import mul
from unicodedata import normalize

YEARS = [''] * 2017

for word in fileinput.input('mots'):
    digits = [ord(l) & 31 for l in normalize('NFKD', word.decode('UTF-8')) if l.isalpha()]
    prod = reduce(mul, digits)
    if prod <= 2016:
        YEARS[prod] = YEARS[prod] or '\n*** %d ***\n' % prod
        YEARS[prod] += '%s : %s = %d\n' % (word.strip(), ' * '.join(map(str, digits)), prod)

print ''.join(YEARS[::-1])[:-1]
