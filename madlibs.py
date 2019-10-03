#Use user input for madlibs. Make an while loop that takes multiple user inputs. Inputs are split() according to commas and stored in a list. Print random items in each list and ask user if they want to repeat the game. If they don't, break the while loops.

#import random module
import random
print("*" * 10)

#create a infinite while loop to repeat code until the conditions are broken.
while True:
    print("Welcome to Shopping List Madlibs!")
    print("You are going shopping and are preparing a list. Enter the items you need from each area of the store, seperated by commas: ")

    #get user input.
    aisleitems = input("What items are needed from the aisle? ")
    meatitems = input("What items are needed from the meat and dairy department? ")
    frozenitems = input("What frozen items are needed? ")

    #split user input at every comma, store split items in a list
    aisle = aisleitems.split(",")
    meat = meatitems.split(",")
    frozen = frozenitems.split(",")

    #print(f) the madlibs statement with random choices from each list above. Do not use concatination for print(f) statements. Below is not the best practice.
    print(f"While going shopping you found" + random.choice(aisle) + " and " + random.choice(meat) + ", but they were out of " + random.choice(frozen))

    again = input("Would you like to try again? Type 'y' for yes or 'n' for no. ")
    #break the while loop if user input equals anything but "y"
    if again != "y":
        break

print("Thank you for using Shopping List Madlibs!")
print("*" * 10)

"""
Questions:
Do you have to assign the input into a list(lines 18-20) or is there a way to take the user input as a list (lines 13-15)?
    No, strings are immutable where lists are mutable. We need to be able to randomize the user input.
"""
