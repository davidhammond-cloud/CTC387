print("I am thinking of a number between 1 and 10:")
x = 0
while (x < 6) or (x > 6):

    x = int(input("Enter a number between 1 and 10: "))
    if (x > 6):
        print("You did not guess my number", "try again")    
    elif (x < 6):
        print("You did not guess my number", "try again")
    elif (x == 6):
        print("You guessed my number")
        


