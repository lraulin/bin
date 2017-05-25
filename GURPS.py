import random

def roll1d():
    return random.randint(1, 6)

print(roll1d())

def rollxd(dice):
    count = 0
    roll = 0
    total = 0
    while count < dice:
        total = total + roll1d()
        count = count + 1
    return total
    
def roll3d():
    return rollxd(3)
     
print(roll3d())
