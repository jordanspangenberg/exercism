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
        if self.remaining_guesses < 0 or self.status == STATUS_WIN:
            raise ValueError("Out of guesses")
        if char in self.word and char not in self.masked:
            for i in range(len(self.word)):
                if self.word[i] == char:
                    self.masked = ''.join((self.masked[:i],char,self.masked[i+1:]))
        else:
            self.remaining_guesses -= 1
        self.status = self.get_status()


    def get_masked_word(self):
        return self.masked


    def get_status(self):
        if self.word == self.masked:
            return STATUS_WIN
        if self.remaining_guesses > 0:
            return STATUS_ONGOING
        else:
            return STATUS_LOSE
        
