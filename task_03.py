#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Finding your interets """

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the amount of your principal? '))
YEARS = int(raw_input('For how many years is this loan being borrowed? '))
PRE_QUALIFIED = raw_input('Are you pre-qualified for this loan? ')
QUALIFIED = PRE_QUALIFIED.upper()[:1]

if QUALIFIED == 'Y':
    if PRINCIPAL > 0 and PRINCIPAL <= 199999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('0.0363')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('0.0404')
        elif YEARS <= 30:
            INTRATE = decimal.Decimal('0.0577')
        else:
            INTRATE = None
    elif PRINCIPAL <= 999999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('0.0302')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('0.0327')
        elif YEARS <= 30:
            INTRATE = decimal.Decimal('0.0466')
        else:
            INTRATE = None
    elif PRINCIPAL >= 1000000:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('0.0205')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('0.0262')
        else:
            INTRATE = None
elif QUALIFIED == 'N':
    if PRINCIPAL <= 199999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('0.0465')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('0.0498')
        elif YEARS <= 30:
            INTRATE = decimal.Decimal('0.0639')
        else:
            INTRATE = None
    elif PRINCIPAL <= 999999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('0.0398')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('0.0408')
        else:
            INTRATE = None
    else:
        INTRATE = None
else:
    INTRATE = None

if INTRATE == None:
    TOTAL = None
else:
    DERATE = decimal.Decimal(INTRATE)
    TOTAL = int(round(PRINCIPAL * (1 + (DERATE / 12)) ** (12 * YEARS)))

print 'Loan Report For: {}'.format(NAME)
print '-' * 60
print '      Principle:{:>15}'.format(PRINCIPAL)
print '      Duration:{:>13}'.format(YEARS)+'yrs'
print '      Pre-qualified?:{:>10}'.format(PRE_QUALIFIED)
print '\n      Total:{:>19}'.format(TOTAL)
