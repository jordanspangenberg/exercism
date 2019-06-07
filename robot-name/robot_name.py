from string import ascii_uppercase
from random import randint, sample, seed

class Robot(object):
    def __init__(self):
        self.name = self.randomName()

    def randomName(self):
        LETTERS = set(ascii_uppercase)
        NUM = randint(100, 999)
        name = ''.join(sample(LETTERS, 2)) + str(NUM)
        return name

    def reset(self):
        seed(randint(1, 10))
        self.name = self.randomName()
