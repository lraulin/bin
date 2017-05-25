# Gets a random height with realistic probability

import random

def random_height():
    print('1 US male 20-29')
    print('2 US female 20-29')

    m = input()
    if m == '1': mean = 177.6
    if m == '2': mean = 163.2

    height_cm = round(random.normalvariate(mean, 7.1))
    inches_total = height_cm * 0.393701
    feet = int(inches_total // 12)
    inches = int(inches_total % 12)
    print("Your character is {} cm tall, or {} feet and {} inches".format(height_cm, feet, inches))
    return height_cm

random_height()
