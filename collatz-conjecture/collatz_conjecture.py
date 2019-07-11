def steps(number):
    if number < 1:
        raise ValueError(f'{number} is not a valid input.')
    count = 0
    while number != 1:
        count += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    
    return count
    
