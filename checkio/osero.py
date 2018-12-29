from typing import List

def checkio(game_result: List[str]) -> str:

    for col in game_result:
        if col == "XXX":
            return "X"
        elif col == "OOO":
            return "O"

    for row in range(len(game_result[0])):
        if game_result[0][row] == game_result[1][row] == game_result[2][row] != ".":
            return game_result[0][row]

    if game_result[0][0] == game_result[1][1] == game_result[2][2] != ".":
        return game_result[0][0]
    elif game_result[0][2] == game_result[1][1] == game_result[2][0] != ".":
        return game_result[0][2]

    return "D"



if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio([
        "X.O",
        "XX.",
        "XOO"]))# == "X", "Xs wins"
    print(checkio([
        "OO.",
        "XOX",
        "XOX"]))# == "O", "Os wins"
    print(checkio([
        "OOX",
        "XXO",
        "OXX"]))# == "D", "Draw"
    print(checkio([
        "O.X",
        "XX.",
        "XOO"]))# == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")