from secrets import randbelow
class Character:

    abilities = ['strength', 'dexterity', \
    'constitution', 'intelligence', 'wisdom', 'charisma']

    def __init__(self):
        for ability in self.abilities:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        li = [randbelow(5)+1 for n in range(4)]
        li.remove(min(li))
        return sum(li)

def modifier(i):
    return (i - 10) // 2
        

    


