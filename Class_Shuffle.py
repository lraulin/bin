#!/usr/bin/env python3

import random

# Student lists by class.
a1 = ['Tiffany', 'Dan1', 'Freddy', 'Jacob', 'William', 'Dan2', 'Dean', 'Kate', 'Julie', 'Sophia', 'Amanda']
a2 = ['Genovefa', 'Erica', 'Nimo', 'Martin', 'Todd', 'Betty', 'Hugh', 'Patrick']
m1 = ['Anna', 'Ji-yeong', 'Jessica', 'Marie', 'Ann', 'Dylan', 'Eric', 'Jung-min', 'Ben']
m2 = ['Nancy', 'Beckam', 'Ronaldo', 'Bidichi', 'Valorie', 'Nicole', 'Ju-seong', 'Ronnie', 'Drogba', 'Jeong-hun', 'Carrie', 'Lisa']
b = ['Ariel', 'Mark', 'Sophia', 'Luke', 'Tiffany', 'David', 'Sylvia', 'Jack', 'Nathan', 'Ben']
g = ['Francisco', 'Julia', 'Antony', 'Kelly', 'Big June', 'Karl', 'Little June', 'Sally', 'Matt', 'Lily', 'Annie', 'Jin', 'Meghan']
y3 = ['Lucy', 'Angela', 'Kassy', 'Alex', 'Collin', 'Shawn', 'Kevin', 'Irene', 'Sarah', 'Chris', 'Shawn']
y = ['Shannon', 'Hannah', 'Erica', 'Harry', 'Kevin', 'Jeff', 'Chris', 'Crystal', 'Ian', 'James']
pb = ['Jack', 'Carol', 'William', 'Sally', 'Carrie', 'Lydia']

x = input('Which class?')
print('Press ENTER to pick a name.')
print('Press CTR-D to quit.')

while input() != 'q':
    if x == 'a1': thisclass = a1[:]
    if x == 'a2': thisclass = a2[:]
    if x == 'm1': thisclass = m1[:]
    if x == 'm2': thisclass = m2[:]
    if x == 'b': thisclass = b[:]
    if x == 'g': thisclass = g[:]
    if x == 'y3': thisclass = y3[:]
    if x == 'y': thisclass = y[:]
    if x == 'pb': thisclass = pb[:]
    #print('a1 = ', a1)
    #print('thisclass = ', thisclass)
    random.shuffle(thisclass)
    while input() != 'q' and thisclass != []:
        print(thisclass[0])
        del thisclass[0]
    print('*** Done...reshuffling. ***')
    
