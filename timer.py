#!/usr/bin/python

import time
import os

sec = 0
minu = 0
cont = 0
while cont != 1:
    print(minu, sec)
    time.sleep(1)
    if sec == 59:
        sec = 0
        minu = minu + 1
    else:
        os.system('clear')
        sec = sec + 1
