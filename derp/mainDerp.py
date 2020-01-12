import random

def isGay(name):
    random.seed(name)
    return random.randint(0,100)