#!/bin/bash

# Set keyboard to Programmer Dvorak with numpad settings
# (Programmer Dvorak when chosen through the GUI doesn't do this)
# Also, swap caps & esc

setxkbmap -layout us -variant dvp -option compose:102 -option numpad:shift3 -option kpdl:semi -option keypad:atm -option caps:swapescape
