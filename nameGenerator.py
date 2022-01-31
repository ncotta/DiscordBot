"""
D&D Name Generation
Author(s): Niklaas Cotta
Created: 01/13/22
"""

import random


def generator(race):

    fileFirst = f"names/{race}_first.txt"
    with open(fileFirst, "r") as f:
        firstnames = [x.strip() for x in f.readlines()]
    f.close()

    name = random.choice(firstnames)

    # These races only have the one name
    if not ((race == "aarakocra") or (race == "genasi") or (race == "halfOrc") or (race == "orc") or (race == "tiefling")):
        fileLast = f"names/{race}_last.txt"
        with open(fileLast, "r") as f:
            lastnames = [x.strip() for x in f.readlines()]
        f.close()

        name += f" {random.choice(lastnames)}"

    # Goliaths have three names
    if race == "goliath":
        with open("names/goliath_last_last.txt", "r") as f:
            lastlastnames = [x.strip() for x in f.readlines()]
        f.close()

        name += f" {random.choice(lastlastnames)}"

    return name
