# x = int(input())
# print(type(x))
import random as rd

p_wins = 0
c_wins = 0

while p_wins < 2 and c_wins < 2:
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    a = input("(enter player A choice): ")
    '''
        FOR MANUAL METHOD 
    b = input("(enter player B choice): ")
    '''
    r_num = rd.randint(0,2)
    if r_num == 0:
        b = "rock"
    elif r_num == 1:
        b = "paper"
    else:
        b = "scissors"

    print(f"(computer selects the option): {b}")
    print("SHOOT!")
    if a == b:
        print("DRAW")
    elif b == "paper" and a == "rock" or b == "scissors" and a == "paper" or b == "rock" and a == "scissors":
        # print("PlayerB wins!!!")  # MANUAL METHOD
        print("Computer Wins!!!")
        c_wins += 1
    elif a == "paper" and b == "rock" or a == "scissors" and b == "paper" or a == "rock" and b == "scissors":
        print("PlayerA wins!!!")
        p_wins += 1
    else:
        print("AYAYAYAYA!! Wrong command capt....")

    # if p_wins 