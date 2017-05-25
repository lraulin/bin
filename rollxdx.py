#!/usr/bin/env python3

# Roll a number of dice (dice) with (sides) number of "sides" (maximum value per roll), and then add a modifier.

def rollxdx(dice, sides, mod):
    roll = mod
    while dice > 0:
        roll = roll + random.randint(1,sides)
        dice = dice - 1
    print(roll)

rollxdx(3,6,0)
