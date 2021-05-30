import random


def roll_dice():
    print('rolling')
    return random.randint(1, 6)


if __name__ == '__main__':
    print('in main')