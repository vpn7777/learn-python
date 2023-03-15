# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    match category:
        case 0:
            return 50 if len(set(dice)) == 1 else 0
        case 1 | 2 | 3 | 4 | 5 | 6:
            return sum(i for i in dice if i == category)
        case 7:
            return sum(dice) if (len(set(dice)) == 2 and
                                 (dice.count(dice[0]) == 2 or
                                  dice.count(dice[0]) == 3)) else 0
        case 8:
            return sum(i * 4 for i in set(dice) if dice.count(i) > 3)
        case 9:
            return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
        case 10:
            return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
        case 11:
            return sum(dice)
