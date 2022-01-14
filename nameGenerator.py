"""
D&D Name Generation
Author(s): Niklaas Cotta
Created: 01/13/22
"""

import random

races = ["aarakocra", "dragonborn", "dwarf", "elf", "genasi", "gnome",
         "goliath", "half-elf", "halfling", "half-orc", "human", "tiefling"]

firstNames = ["Stephanie", "Zuul", "Balfred", "Schnabs", "Beeyorn", "Daved", "Jeel", "Tomey"]
lastNames = ["Windstrider", "Stoneseeker", "Smith", "Hightower", "Ramshorn"]


def generator(race):
    return random.choice(firstNames) + " " + random.choice(lastNames)
