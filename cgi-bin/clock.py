#!/usr/bin/env python
import datetime
import os

time1 = datetime.datetime.now()
hours = time1.hour
minutes = time1.minute
print hours, minutes
if hours > 10 and hours < 24 :
    if hours > 12 :
        mf = ' P M'
        hours -= 12
    else :
        mf = ' A M'
    if minutes == 0:
        minutes = 'o clock'
    elif minutes > 0 and minutes < 10:
            minutes = 'o' + str(minutes)
    os.system('espeak "the time is ' + str(hours) +' ' + str(minutes) + mf +'"')
