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

while (inpt != 'q'):
    critsuc = 0
    critfail = 0
    inpt = input('Reaction Modifier: ')
    if inpt == '':
        mod = 0
    else:
        mod = int(inpt)
    roll = roll3d6()
    result = roll + mod
    print(result)

    if result <= 0:
        print('Disastrous: The NPC hates the PCs and acts in their worst interest.')
    elif result <= 3:
        print('Very Bad: The NPC dislikes the PCs and acts against them if it’s convenient to do so')
    elif result <= 6:
        print ('Bad: The NPC cares nothing for the PCs and acts against them if he can profit by doing so.')
    elif result <= 9:
        print('Poor: The NPC is unimpressed. He may become hostile if there is much profit in it, or little danger.')
    elif result <= 12:
        print ('Neutral: The NPC ignores the PCs as much as possible. He is totally uninterested.')
    elif result <= 15:
        print('Good: The NPC likes the PCs and is helpful within reasonable, everyday limits.')
    elif result <= 18:
        print ('Very Good: The NPC thinks highly of the PCs and is quite helpful and friendly.')
    else:
        print('Excellent: The NPC is extremely impressed by the PCs, and acts in their best interests at all times, within the limits of his own ability.')
        
    print()
