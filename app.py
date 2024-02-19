import currency_roulette_game
import guess_game
import memory_game
from guess_game import play
from memory_game import play
from currency_roulette_game import play
from score import add_score
def welcome():
    while True:
        # user will be in the loop for all "invalid" inputs.
        # can only break the loop if input is "valid")
        userinput = input("what is your name? ")

        #check - all letters?
        if userinput.isalpha() == True:
            break # valid input -> break the loop

        # check - empty input?
        elif userinput == "" or userinput.isspace() == True:
            continue # invlid input -> ask input again

        else: # input = not only letters + not empty

            # check- all string is digits or float?
            try:
                int(userinput) # only invalid input can be converted
                print("your are not a number, you are a free man :), please choose again")
                continue

            # check - include any letter? (>=1)???
            except:
                containsLetter = False
                containsNonLetter = False

            for i in userinput:
                if i.isalpha() == True:
                 containsLetter = True
                else:
                    containsNonLetter = True

            if containsLetter == False and containsNonLetter == True:
                # no letters found in input
                continue # invlid input -> ask input again
            else:
                break # valid input -> break the loop

    print("Hi " + userinput + " and welcome to the World of Games: The Epic Journy")

def start_play1():

    games = {"1":"1 - Memory Game","2":"2 - Geuss Game","3":"3 - Currency Roulette"}

    # choose a game number
    print("Please choose a game to play:")
    for games_number in games:
        print(games[games_number])

    gameType = None
    while gameType not in range(1, len(games) + 1):
        try:
            gameType = int(input("choose number: "))
        except: # invalid input
            print("not a valid game number to play")

    # choose a game Difficulty
    levelDifficulty = None
    while levelDifficulty not in range(1, 6):
        try:
            levelDifficulty = int(input("Please select level difficulty 1-5: "))
        except:
            print("not a valid level difficulty to choose")
    return gameType, levelDifficulty

def start_play():
    game_configuration = start_play1()
    type = int(game_configuration[0])
    difficulty = int(game_configuration[1])
    if type == 1:
        winner = memory_game.play(difficulty)
        if winner == True:
            add_score(difficulty)
    elif type == 2:
        winner = guess_game.play(difficulty)
        if winner == True:
            add_score(difficulty)
    elif type == 3:
        winner = currency_roulette_game.play(difficulty)
        if winner == True:
            add_score(difficulty)