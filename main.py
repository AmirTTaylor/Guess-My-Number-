"""
1: Ask User what difficulty they want to play (Easy 1-10, Medium 1-50, Hard 1 - 100, Impossible 1 - 1000)
2: Generate random number based on difficulty chosen
3: Allo infinite guesses using while loop
4: Also allow option to give up
"""

import random as r

# Menu
print("==================="+
      "\n Guess The Number!!"+
      "\n===================")

#Get Difficulty
print("\nChoose your difficulty: ")

dif = int(input("\n1) Easy (1-10)"+
                "\n2) Medium (1-50)"+
                "\n3) Hard (1-100)"+
                "\n4) IMPOSSIBLE!"+
                "\nAnswer Here: "))

#Generate the Number Based on chosen difficulty 
if dif == 1:

    num = r.randint(1,10)
    max_num = 10

elif dif == 2:

    num = r.randint(1,50)
    max_num = 50

elif dif == 3:

    num = r.randint(1,100)
    max_num = 100

elif dif == 4:

    num = r.randint(1,1000)
    max_num = 1000

quit = 'Y'

#Start Guessing and Keep Going until they choose to quit
while quit.lower() != 'n':

    guess = int(input(f"Guess a number 1 - {max_num}: "))

    if guess == num:
        print("\nGreat Guess You Win!!")
        quit = 'n'
    else:
        print("\nThat's not it!")
        quit = input("\nGuess Again? ('Y' or 'N'): ").strip().lower()
