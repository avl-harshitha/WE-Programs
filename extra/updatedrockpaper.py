import sys

delimiter = ", "
game_dict = dict(zip(["win", "lose", "draw"], [0] * 3))


def decide_game(game):
    winningcomb = "RSPR"
    if game == game[::-1]:
        game_dict["draw"] += 1
    elif winningcomb.find(game) != -1:
        game_dict["win"] += 1
    else:
        game_dict["lose"] += 1


def find_gameplays(gamestr):
    for game in gamestr.split(", "):
        decide_game(game)
    return print_gameplays(game_dict)


def print_gameplays(game_dict):
    prefix = ["+", "-", "="]
    game_results = list(game_dict.values())
    for i in range(len(prefix)):
        print(prefix[i], game_results[i], sep="", end=" ")



# find_gameplays(sys.argv[1])
find_gameplays("RP, RR, SP, SR")

