# Rock paper scissors game
# Author: Todimu Isewon

"""
    I wrote tests for the functions printActualWord and
    pickWinner in order to ensure they were working in any use
    case. Both test files are in the repository.
"""

from random import choice

# creating possible choices list
possibleChoices: list = ["r", "p", "s"]

# getting user choice
userChoice: str = input("Enter R, P or S :  ").lower()

# ensuring choice is valid
while userChoice not in possibleChoices:
    print("Invalid response, enter valid response \n")
    userChoice: str = input("Enter R, P or S :  ").lower()

# getting computer choice
computerChoice: str = choice(possibleChoices)


# print out words in full
def printActualWord(letter: str):
    if letter == "r":
        return "rock"

    elif letter == "p":
        return "paper"

    elif letter == "s":
        return "scissors"


# printing user and computer choices
print("Player ({0}) : computer ({1}) \n"
      .format(printActualWord(userChoice), printActualWord(computerChoice)))


# creating winner picking function
def pickWinner(choiceUser: str, cpuChoice: str) -> str:
    if choiceUser == cpuChoice:
        return "tie"

    elif choiceUser == "r":
        if cpuChoice == "p":
            return "{0} gets covered by {1}, computer wins".format(choiceUser, cpuChoice)
        else:
            return "{0} crushes s, you win !".format(choiceUser)

    elif choiceUser == "p":
        if cpuChoice == "s":
            return "{0} gets cut by {1}, computer wins".format(choiceUser, cpuChoice)
        else:
            return "{0} covers r, you win !".format(choiceUser)

    elif choiceUser == "s":
        if cpuChoice == "r":
            return "{0} gets crushed by {1}, computer wins".format(choiceUser, cpuChoice)
        else:
            return "{0} cuts p, you win !".format(choiceUser)


# ensure that game continues when there is a tie
gameResult: str = pickWinner(userChoice, computerChoice)

while gameResult == "tie":
    print("We have a tie, lets go again !!!")
    userChoice: str = input("Enter R, P or S :  ").lower()

    while userChoice not in possibleChoices:
        print("Invalid response, enter valid response \n")
        userChoice: str = input("Enter R, P or S :  ").lower()

    computerChoice: str = choice(possibleChoices)

    print("Player ({0}) : computer ({1}) \n"
          .format(printActualWord(userChoice), printActualWord(computerChoice)))

    gameResult = pickWinner(userChoice, computerChoice)

print(gameResult)
