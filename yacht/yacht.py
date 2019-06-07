import collections

# Score categories
# Change the values as you see fit
YACHT =  (lambda x: 50 if len(set(x)) == 1 else 0)
ONES =   (lambda x: sum(n for n in x if n == 1))
TWOS =   (lambda x: sum(n for n in x if n == 2))
THREES = (lambda x: sum(n for n in x if n == 3)) 
FOURS =  (lambda x: sum(n for n in x if n == 4)) 
FIVES =  (lambda x: sum(n for n in x if n == 5)) 
SIXES =  (lambda x: sum(n for n in x if n == 6)) 
FULL_HOUSE = (lambda x: sum(n for n in x) if fullHouse(x) else 0)
FOUR_OF_A_KIND = (lambda x:next((n*4 for n in x if x.count(n) >= 4),0))
LITTLE_STRAIGHT = (lambda x: 30 if collections.Counter(x) == collections.Counter(list(range(1, 6))) else 0)
BIG_STRAIGHT = (lambda x: 30 if collections.Counter(x) == collections.Counter(list(range(2, 7))) else 0)
CHOICE = (lambda x: sum(n for n in x))


def score(dice, category):
    return category(dice)


def fullHouse(li):
    for n in set(li):
        return len(set(li)) == 2 and li.count(n) == 2 or li.count(n) == 3
