#!/usr/bin/env python3

import random

def fudgedice():
    dice = 4
    roll = 0
    while dice > 0:
        roll = roll + random.randint(-1,1)
        dice = dice - 1
    return roll

def contest(p1skill, p2skill):
    p1roll = fudgedice() + p1skill
    p2roll = fudgedice() + p2skill
    if p1roll > p2roll:
        print('You win by', p1roll - p2roll)
    if p2roll > p1roll:
        print('You lose by', p2roll - p1roll)
    if p1roll == p2roll:
        print('Stalemate!')

input1 = input('What is your skill?')
p1skill = int(input1)
input2 = input('What is you opponents skill?')
p2skill = int(input2)
while input() != 'n':
    contest(p1skill, p2skill)
