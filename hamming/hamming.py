def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The given sequence is of unequal length.")
    hamCount = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            hamCount += 1

    return hamCount

