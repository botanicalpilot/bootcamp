#file saved as madlibs2.property
#import random module
import random
print("*" * 10)

#create a infinite while loop to repeat code until the conditions are broken.
while True:
    print("Welcome to Shopping List Madlibs!")
    print("You are going shopping and are preparing a list. Enter the items you need from each area of the store, seperated by commas")

    #get user input. This
    aisleitems = input("What items are needed from the aisle? ")
    meatitems = input("What items are needed from the meat and dairy department? ")
    frozenitems = input("What frozen items are needed? ")

    #split user input at ever comma, store split items in a list
    aisle = aisleitems.split(",")
    meat = meatitems.split(",")
    frozen = frozenitems.split(",")

    #printf the madlibs statement with random choices from each list above.
    print(f"While going shopping you found" + random.choice(aisle) + " and " + random.choice(meat) + ", but they were out of " + random.choice(frozen))
    
    again = input("Would you like to try again? Type 'y' for yes or 'n' for no. ")
    #break the while loop if user input equals anything but "y"
    if again != "y":
        break

print("Thank you for using Shopping List Madlibs!")
print("*" * 10)
