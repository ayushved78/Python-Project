from pickle import NONE
import random as rd

num = rd.randint(0,10)
print(num)

# n = int(input("Guess a number between 0 to 10: "))
n = NONE
# ans = "y"

# MY LOGIC -> FAILED
'''
while ans != "n":
    while n != num:
        n = input("Guess a number between 0 to 10: ")
        if n != num:
            if num >= 0 and num <= 5:
               print("Too low, try again")
            else:
                print("Too high, try again")
        else:
            print("You got it")
            ans = input("DO you want to continue?(y/n) ")
'''     

# COLT LOGIC
# while ans == "y":
# if ans == "y":
# if ans == "y":
while True:
    n = int(input("Guess a number between 0 to 10: "))
    if n == num:
        print("You got it")
        ans = input("Do you want to continue? (y/n) ")
        if ans == "y":
            num = rd.randint(0,10)
            n = None
        else:
            print("Thank You!")
            break

    elif n < num:
        print("Too low, try again")
        ans = "y"
    else:
        print("Too high, try again")
        # ans = "y"


