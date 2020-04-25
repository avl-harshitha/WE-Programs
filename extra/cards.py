import random

diamonds = list(range(2, 15))
random.shuffle(diamonds)
user = list(range(2, 15))
computer = list(range(2, 15))

def showDiamondCard() -> int:
    return diamonds.pop()

def computerBid(diamond):
    compcard = random.choice(computer)
    computer.remove(compcard)
    return compcard

def decideWinner(userScore, compScore):
    return ["User won", "Computer won"][userScore <= compScore]

def UserBid():
    print("which card?")
    userCard = int(input())
    user.remove(userCard)
    return userCard
 
def updateScores(userScore,compScore,user,comp):
    return userScore+user,compScore+comp

def decideBid(dCard, userCard, pcCard):
    pcScore = 0
    userScore = 0
    if userCard == pcCard:
        userScore += dCard // 2
        pcScore += dCard // 2
        print("it's a draw")
    elif userCard > pcCard:
        userScore += dCard
        print("You got the card")
    else:
        pcScore += dCard
        print("I got the card")
    return userScore, pcScore

def displayBid(userCard, compCard):
    print(userCard, compCard)

def scoreBoard(user, computer):
    print("You\tME\n",user,"\t",computer)


def game():
    userScore = 0
    compScore = 0
    while len(diamonds) > 0 and userScore <= compScore + sum(diamonds) and compScore <= userScore + sum(diamonds):
        diamondCard = showDiamondCard()
        print(diamondCard)
        compCard = computerBid(diamondCard)
        userCard = UserBid()
        displayBid(userCard, compCard)
        user, comp = decideBid(diamondCard, userCard, compCard)
        userScore,compScore = updateScores(userScore,compScore,user,comp)
        scoreBoard(userScore, compScore)
    return decideWinner(userScore, compScore)

print(game())
