import random
es = 'null'
inpt = 'null'

def roll_d6(x):
    result = 0
    for i in range(0, x):
        result += random.randint(1, 6)
        print(result)
    return result

roll_d6(3)

##while (inpt != 'q'):
##    critsuc = 0
##    critfail = 0
##    inpt = input('Effective Skill: ')
##    if inpt == '':
##        efskill = int(10)
##    else:
##        efskill = int(inpt)
##    roll = roll3d6()
##    rolldegree = efskill - roll
##    
##    if efskill >= 16 and roll <= 6:
##        critsuc = 1
##    elif efskill == 15 and roll <= 5:
##        critsuc = 1
##    elif roll <= 4:
##        critsuc = 1
##    else:
##        critsuc = 0
##
##    if roll >= (efskill + 10):
##        critfail = 1
##    elif roll >= 17 and efskill <= 15:
##        critfail = 1
##    elif roll >= 18:
##        critfail = 1
##    else:
##        critfail = 0
##    
##    if rolldegree < 0:
##        print('FAILURE! (ㅠ.ㅠ)')
##    else:
##        print('SUCEESS! \(^.^)/')
##    print('Effective Skill', efskill, '- Result', roll, '= Rolled Degree', rolldegree)
##    if critsuc == 1:
##        print('♦♦♦♦ ♥♥♥♥ ☼☼☼☼☼ ¡¡¡CRITICAL SUCCESS!!! ☼☼☼☼☼ ♥♥♥♥ ♦♦♦♦')
##        print('♦♦♦♦ ♥♥♥♥ ☼☼☼☼☼ ¡¡¡CRITICAL SUCCESS!!! ☼☼☼☼☼ ♥♥♥♥ ♦♦♦♦')
##        print('♦♦♦♦ ♥♥♥♥ ☼☼☼☼☼ ¡¡¡CRITICAL SUCCESS!!! ☼☼☼☼☼ ♥♥♥♥ ♦♦♦♦')
##    if critfail == 1:
##        print('♠♠♠♠♠ CRITICAL FAILURE! YOU SUCK!!!! ♠♠♠♠♠')
##        print('♠♠♠♠♠ CRITICAL FAILURE! YOU SUCK!!!! ♠♠♠♠♠')
##        print('♠♠♠♠♠ CRITICAL FAILURE! YOU SUCK!!!! ♠♠♠♠♠')
##        
##    print()
##
