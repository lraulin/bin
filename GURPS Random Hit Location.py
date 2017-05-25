import random
es = 'null'
inpt = 'null'
def rolld6():
    n = random.randint(1, 6)
    return n
def roll3d6():
    r1 = rolld6()
    r2 = rolld6()
    r3 = rolld6()
    total = r1 + r2 + r3
    print(r1, '+', r2, '+', r3, '=', total)
    return total

while input() != 'q':
    roll = roll3d6()
    if roll == 3:
        flip = random.randint(0, 1)
        if flip == 0:
            print('Right Eye')
        else:
            print('Left Eye')
    if roll == 3 or roll == 4:
        print('Skull')
    elif roll == 5:
        print('Face')
    elif roll == 6 or roll == 7:
        print ('Right Leg')
    elif roll == 8:
        print ('Right Arm')
        flip = random.randint(1, 6)
        if flip ==1 or flip == 2:
            print('Forearm')
        if flip == 3:
            print('Elbow')
        if flip == 4 or flip == 5:
            print('Bicep')
        if flip == 6:
            print('Shoulder')
    elif roll == 9 or roll == 10:
        print ('Torso')
    elif roll == 11:
        print ('Groin')
    elif roll == 12:
        print ('Left Arm')
        flip = random.randint(1, 6)
        if flip ==1 or flip == 2:
            print('Forearm')
        if flip == 3:
            print('Elbow')
        if flip == 4 or flip == 5:
            print('Bicep')
        if flip == 6:
            print('Shoulder')
    elif roll == 13 or roll == 14:
        print ('Left Leg')
    elif roll == 15:
        flip = random.randint(0, 1)
        if flip == 0:
            print('Right Hand')
        else:
            print('Left Hand')
    elif roll == 16:
            flip = random.randint(0, 1)
            if flip == 0:
                print('Right Foot')
            else:
                print('Left Foot')
    elif roll == 17:
        print('Neck')
    else:
        print('Vitals')
