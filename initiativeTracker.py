"""
Author(s): Niklaas Cotta
Date Created: 2/3/22
Desc: An initiative tracker
"""


class Initiative:
    def __init__(self):
        self.initiative = [{"name": "Schnibs", "turn": 21},
                           {"name": "Stephanie", "turn": 18},
                           {"name": "Bjorn", "turn": 15},
                           {"name": "Trolloc 1", "turn": 17},
                           {"name": "Ogre 1", "turn": 12},
                           {"name": "Scary Person", "turn": 24}]

    def initialize(self):
        self.initiative = sorted(self.initiative, key=lambda i: i["turn"])

    def turn(self):
        going = self.initiative.pop()
        self.initiative.insert(0, going)

    def printChars(self):
        reversedInitiative = self.initiative[::-1]
        i = 1
        for character in reversedInitiative:
            print(f"#{i}: {character['name']} (initiative: {character['turn']})")
            i += 1


if __name__ == '__main__':
    turns = Initiative()
    turns.initialize()
    turns.printChars()
    turns.turn()
    turns.turn()
    print("===============================")
    turns.printChars()
