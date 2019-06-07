from math import pow
def is_armstrong_number(number):
    numberStr = str(number)
    length = len(numberStr)
    return number == sum([pow(int(n), length) for n in numberStr])
