import random

def isGay(name):
    random.seed(name)
    return random.randint(0,100)

def drinkGame(inNumber):
    number = round(random.random() * 11)
    return abs(number - inNumber), number
