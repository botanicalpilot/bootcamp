import random
import time

def wait():
    ticker = int(0)
    while ticker < 3:
        print(".")
        time.sleep(0.5)
        ticker += 1
def eightball():
    question = input("What do you want to ask the magic eight ball")
    preditions = ["No", "Yep, probably", "Sorry, not likely"]
    wait()
    print(random.choice(preditions))

eightball()
