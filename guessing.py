import random

def game(chances):
    rNum = random.randint(1,100)
    while chances != 0:
       
        try:
           guess = int(input("guess the number:> "))
        except ValueError:
           print("please insert a valid number")
           continue

        if guess == rNum:
            print("correct!!")
            break
        elif guess > rNum:
            print("lower!")
            chances -= 1
            print(f"number of chances left: {chances}\n")
        elif guess < rNum:
            print("higher!")
            chances -= 1
            print(f"number of chances left: {chances}\n")
    else:
        print("sorry you lost!")
        print(f"the number was {rNum}")

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n""")

print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")

try:
    userInput = int(input("choose the difficulty pls :> "))
except ValueError:
    print("please insert a valid number")
    exit()

if userInput == 1:
    print("\nGreat! You have selected the Easy difficulty level.\nLet's start the game!\n")
    chances = 10
    game(chances)

elif userInput == 2:
    print("\nGreat! You have selected the Medium difficulty level.\nLet's start the game!\n")
    chances = 5
    game(chances)

elif userInput == 3:
    print("\nGreat! You have selected the Hard difficulty level.\nLet's start the game!\n")
    chances = 3
    game(chances)
else:
    print("Invalid difficulty level chosen. Exiting the game.")
