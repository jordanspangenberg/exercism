
import re

# this is slahmar's solution from 
# https://exercism.io/tracks/python/exercises/isbn-verifier/solutions/a243df1b079d42be84a3f9bdb6b3343f
def check_isbn_formula(digits):
    numbers_to_mult = list(map(int, digits))
    return sum([factors[0] * factors[1] for factors in zip(numbers_to_mult, range(10,0,-1))]) % 11 == 0

def verify(isbn):
    stripped_isbn = isbn.replace("-", "")
    if not re.compile("[0-9]{9}([0-9]|X)$").match(stripped_isbn):
        return False
    else:
        digits = list(stripped_isbn)
        if digits[-1] == 'X':
            digits[len(digits)-1] = '10'
        return check_isbn_formula(digits)

print(verify('123456789X'))