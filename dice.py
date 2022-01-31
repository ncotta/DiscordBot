"""
Dice Rolling Program
Author(s): Niklaas Cotta
Created: 01/13/22
"""

# TODO:
# advantages

import random

diceTypes = ["d100", "d20", "d12", "d10", "d8", "d6", "d4", "d2"]


def roll(diceType):
    critHit = False
    critMiss = False

    if diceType.lower().strip() not in diceTypes:
        return None

    else:
        result = random.randint(1, int(diceType[1:]))

    if int(result) == 1:
        critMiss = True
    elif int(result) == int(diceType[1:]):
        critHit = True

    return result  # f"You rolled a {diceType} and got a {result}!"


def multiroll(diceType, n):
    total = 0
    string = f"You rolled {n if n > 1 else 'a'} {diceType}{'s' if n > 1 else ''} and got a"

    if not 0 < n < 100:
        return "No dice!\n"

    for i in range(n):
        result = roll(diceType)
        if not result:
            return "No dice!\n"
        string += f"{' +' if i > 0 else ''} {result}"
        total += int(result)

    if n != 1:
        string += f" = {total}!"

    return string


if __name__ == '__main__':
    print(multiroll("d100", 1))
