#!/usr/bin/python

import time
import os

sec = 0
minu = 0
hour = 0
cont = 0
while cont != 1:
    print(minu, sec)
    time.sleep(1)
    if sec == 59:
        if minu == 59:
            minu = 0
            hour += 1
        sec = 0
        minu = minu + 1
    else:
        os.system('clear')
        sec = sec + 1
