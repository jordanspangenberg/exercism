from string import ascii_uppercase as letters


def is_valid(isbn: str) -> bool:
    _isbn = isbn.replace('-', '')
    if len(_isbn) != 10:
        return False
    multArr = [x for x in range(1,11)]
    num = 0
    for i in range(10):
        if _isbn[i] in letters:
            if _isbn[-1] == 'X' and i == 9:
                pass
            else: 
                return False
        x = 10 if _isbn[i] == 'X' else int(_isbn[i])
        num += x * multArr[(i+1)*-1]
    return num % 11 == 0
