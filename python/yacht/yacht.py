# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = None


def dice_side(dice, side):
    return sum(i for i in dice if i == side)


def score(dice, category):
    sides = ["ONES", "TWOS", "THREES", "FOURS", "FIVES", "SIXES"]
    if category == "YACHT":
        return 50 if len(set(dice)) == 1 else 0
    elif category in sides:
        return dice_side(dice, sides.index(category) + 1)
    elif category == "FULL_HOUSE":
        return sum(dice) if (len(set(dice)) == 2 and
                             (dice.count(dice[0]) == 2 or
                              dice.count(dice[0]) == 3)) else 0
    elif category == "FOUR_OF_A_KIND":
        for i in dice:
            if dice.count(i) >= 4:
                return i * 4
            else:
                return 0
    elif category == "LITTLE_STRAIGHT":
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == "BIG_STRAIGHT":
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    else:
        return sum(dice)
