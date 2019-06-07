def is_pangram(sentence):
    count = 0
    charArr = list(sentence.lower())
    alreadySeen = []
    for character in charArr:
        asciiCode = ord(character) 
        if (asciiCode >= 97 and asciiCode <= 122):
            if not asciiCode in alreadySeen:
                alreadySeen.append(asciiCode)
                count += 1
    return count == 26


