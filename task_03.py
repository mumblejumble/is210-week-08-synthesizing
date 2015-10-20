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
    if PRINCIPAL <= 199999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('3.63')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('4.04')
        elif YEARS <= 30:
            INTRATE = decimal.Decimal('5.77')
    elif PRINCIPAL <= 999999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('3.02')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('3.27')
        elif YEARS <= 30:
            INTRATE = decimal.Decimal('4.66')
    elif PRINCIPAL >= 1000000:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('2.05')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('2.62')
elif QUALIFIED == 'N':
    if PRINCIPAL <= 199999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('4.65')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('4.98')
        elif YEARS <= 30:
            INTRATE = decimal.Decimal('6.39')
    elif PRINCIPAL <= 999999:
        if YEARS >= 1 and YEARS <= 15:
            INTRATE = decimal.Decimal('3.98')
        elif YEARS <= 20:
            INTRATE = decimal.Decimal('4.08')
else:
    INTRATE = None

if INTRATE is None:
    TOTAL = int(round((PRINCIPAL * ((1 + (None / 12)) ** (12 * YEARS)))))
else:
    CONVERT = decimal.Decimal(INTRATE) / 100
    TOTAL = int(round((PRINCIPAL * ((1 + (CONVERT / 12)) ** (12 * YEARS)))))

print 'Loan Report For: {}'.format(NAME)
print '-' * 60
print '      Principle:{:>15}'.format(PRINCIPAL)
print '      Duration:{:>13}'.format(YEARS)+'yrs'
print '      Pre-qualified?:{:>10}'.format(PRE_QUALIFIED)
print '\n      Total:{:>19}'.format(TOTAL)
