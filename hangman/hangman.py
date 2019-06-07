import sys

# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        if '_' in word:
            raise ValueError('Hangman word cannot contain underscore')
        self.word = word
        self.masked = ''.join(['_' if l != ' ' else ' ' for l in self.word])


    def guess(self, char):
        guesses = []
        if self.remaining_guesses < 0:
            raise ValueError()
        if char in self.word:
            guesses.append(char)
            self.masked = ''.join([char if l == char else l for l in self.word])
        else:
            self.remaining_guesses -= 1
        self.status = self.get_status()


    def get_masked_word(self):
        return self.masked


    def get_status(self):
        if self.remaining_guesses > 0:
            return STATUS_ONGOING
        if self.word == self.masked:
            return STATUS_WIN
        else:
            return STATUS_LOSE
        
