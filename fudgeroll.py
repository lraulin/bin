#!/usr/bin/env python3

import random

skill = 0

def fudgedice(skill):
    dice = 4
    roll = 0
    if skill == "": skill = 0
    while dice > 0:
        roll = roll + skill + random.randint(-1,1)
        dice = dice - 1
    if roll >= 4: print('+', roll, ' Legendary', sep='')
    if roll == 3: print('+', roll, ' Superb', sep='')
    if roll == 2: print('+', roll, ' Great', sep='')
    if roll == 1: print('+', roll, ' Good', sep='')
    if roll == 0: print('+', roll, ' Fair', sep='')
    if roll == -1: print(roll, ' Mediocre', sep='')
    if roll == -2: print(roll, ' Poor', sep='')
    if roll == -3: print(roll, ' Terrible', sep='')
    if roll <= -4: print(roll, ' Abysmal', sep='')

while input() != 'q':
    fudgedice(input())
