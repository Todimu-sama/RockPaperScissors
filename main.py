# Rock paper scissors game
# Author: Todimu Isewon

from random import choice

# creating possible choices list
possibleChoices: list = ["rock", "paper", "scissors"]

# getting user choice
userChoice: str = input("Enter Rock, Paper or Scissors :  ").lower()

# ensuring choice is valid
while userChoice not in possibleChoices:
    print("Invalid response, enter valid response \n")
    userChoice: str = input("Enter Rock, Paper or Scissors :  ").lower()

# getting computer choice
computerChoice: str = choice(possibleChoices)

# printing user and computer choices
print("Player ({0}) : computer ({1}) \n".format(userChoice, computerChoice))


# creating winner picking function
def pickWinner(choiceUser: str, cpuChoice: str) -> str:
    if choiceUser == cpuChoice:
        return "tie"

    elif choiceUser == "rock":
        if cpuChoice == "paper":
            return "{0} gets covered by {1}, computer wins".format(choiceUser, cpuChoice)
        else:
            return "{0} crushes scissors, you win !".format(choiceUser)

    elif choiceUser == "paper":
        if cpuChoice == "scissors":
            return "{0} gets cut by {1}, computer wins".format(choiceUser, cpuChoice)
        else:
            return "{0} covers rock, you win !".format(choiceUser)

    elif choiceUser == "scissors":
        if cpuChoice == "rock":
            return "{0} gets crushed by  {1}, computer wins".format(choiceUser, cpuChoice)
        else:
            return "{0} cuts paper, you win !".format(choiceUser)


# ensure that game continues when there is a tie

gameResult: str = pickWinner(userChoice, computerChoice)

while gameResult == "tie":
    print("We have a tie, lets go again !!!")
    userChoice: str = input("Enter Rock, Paper or Scissors :  ").lower()

    while userChoice not in possibleChoices:
        print("Invalid response, enter valid response \n")
        userChoice: str = input("Enter Rock, Paper or Scissors :  ").lower()

    computerChoice: str = choice(possibleChoices)

    print("Player ({0}) : computer ({1}) \n".format(userChoice, computerChoice))

    gameResult = pickWinner(userChoice, computerChoice)

print(gameResult)
