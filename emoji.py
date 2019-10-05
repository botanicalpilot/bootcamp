import random

print("Welcome to the Emoji Maker")

def emoji_assembler():
    eyes = [':', '=', '>:']
    nose = ['-', 'X']
    mouth = ['D', '|', 'P']
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

emoji_assembler()
