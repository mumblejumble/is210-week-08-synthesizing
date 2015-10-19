#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module helps you choose colors """


BASEQ = 'Which base color, '
ACCENTQ = 'Which accent color, '
HIGHLIGHTQ = 'Which highlight color, '
MYERROR = 'Sorry, the colors you chose is not valid, please try again.'

BASE = raw_input(BASEQ + '"Seattle Gray" or "Manatee"? ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input(ACCENTQ + '"Ceramic Glaze" or "Cumulus Nimbus"? ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input(HIGHLIGHTQ + '"Basically White" or "White"? ')
    elif ACCENT == 'Cumnulus Nimbus':
        HIGHLIGHT = raw_input(HIGHLIGHTQ + '"Off-White" or "Paper White"? ')
    else:
        print MYERROR
elif BASE == 'Manatee':
    ACCENT = raw_input(ACCENTQ + '"Platinum Mist" or "Spartan Sage"? ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input(HIGHLIGHTQ + '"Bone White" or "Just White"? ')
    elif ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input(HIGHLIGHTQ + '"Fractal White" or "Not White"? ')
    else:
        print MYERROR
else:
    print MYERROR
print 'Your selected colors are {}, {}, and {}.'.format(BASE, ACCENT, HIGHLIGHT)
