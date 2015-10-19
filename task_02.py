#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Alarm Colock """


DAY = (raw_input('What day is it? ')).lower()[:3]
TIME = int(raw_input('What time is it? '))

SNOOZE = True if (DAY is 'sat' or 'sun') and TIME < 600 else 'Beep!' * 5
print SNOOZE
