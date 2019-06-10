import sys

delimiter = ", "
gamestringconst = "RSPR"
game_dict = dict(zip(["win", "lose", "draw"], [0] * 3))



def clean_input(inputstr):
    return inputstr.replace(delimiter, "")


def decide_match(gamestr, index):
    if gamestr[index] == gamestr[index + 1]:
        game_dict["draw"] += 1
    elif gamestringconst.find(gamestr[index:index + 2]) != -1:
        game_dict["win"] += 1
    else:
        game_dict["lose"] += 1


def find_gameplays(gamestr):
    gamestr = clean_input(gamestr)
    for i in range(0, len(gamestr), 2):
        decide_match(gamestr, i)
    return print_gameplays(game_dict)


def print_gameplays(game_dict):
    prefix = ["+", "-", "="]
    game_results = list(game_dict.values())
    for i in range(len(prefix)):
        print(prefix[i], game_results[i], sep="", end=" ")



# find_gameplays(sys.argv[1])
find_gameplays("RP, RR, SP, SR")

