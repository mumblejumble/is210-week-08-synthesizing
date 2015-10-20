#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Finding your interets """

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the principal of the loan? '))
YEARS = int(raw_input('For how long is this being borrowed? '))
PRE_QUALIFIED = raw_input('Are you pre-qualified? ')
QUALIFIED = PRE_QUALIFIED.lower()[:1]

if QUALIFIED == 'y':
    if PRINCIPAL > 0 and PRINCIPAL <= 199999:
        if YEARS >= 1 and YEARS <= 15:
            IRATE = decimal.Decimal('0.0363')
        elif YEARS <= 20:
            IRATE = decimal.Decimal('0.0404')
        elif YEARS <= 30:
            IRATE = decimal.Decimal('0.0577')
        else:
            IRATE = None
    elif PRINCIPAL <= 999999:
        if YEARS >= 1 and YEARS <= 15:
            IRATE = decimal.Decimal('0.0302')
        elif YEARS <= 20:
            IRATE = decimal.Decimal('0.0327')
        elif YEARS <= 30:
            IRATE = decimal.Decimal('0.0466')
        else:
            IRATE = None
    elif PRINCIPAL >= 1000000:
        if YEARS >= 1 and YEARS <= 15:
            IRATE = decimal.Decimal('0.0205')
        elif YEARS <= 20:
            IRATE = decimal.Decimal('0.0262')
        else:
            IRATE = None
    else:
        IRATE = None
elif QUALIFIED == 'n':
    if PRINCIPAL > 0 and PRINCIPAL <= 199999:
        if YEARS >= 1 and YEARS <= 15:
            IRATE = decimal.Decimal('0.0465')
        elif YEARS >= 16 and YEARS <= 20:
            IRATE = decimal.Decimal('0.0498')
        elif YEARS >= 21 and YEARS <= 30:
            IRATE = decimal.Decimal('0.0639')
        else:
            IRATE = None
    elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
        if YEARS >= 1 and YEARS <= 15:
            IRATE = decimal.Decimal('0.0398')
        elif YEARS >= 16 and YEARS <= 20:
            IRATE = decimal.Decimal('0.0408')
        else:
            IRATE = None
    else:
        IRATE = None
else:
    IRATE = None

if IRATE is None:
    TOTAL = None
else:
    TOTAL = int(round(PRINCIPAL * (1 + IRATE / 12) ** (12 * YEARS)))

print 'Loan Report For: {}'.format(NAME)
print '-' * 60
print '      Principle:{:>15}'.format(PRINCIPAL)
print '      Duration:{:>13}'.format(YEARS)+'yrs'
print '      Pre-qualified?:{:>10}'.format(PRE_QUALIFIED)
print '\n      Total:{:>19}'.format(TOTAL)
