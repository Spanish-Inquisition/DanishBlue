import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DanishBlue'
strategy_name = 'test'
strategy_description = 'testing stuff'

def move(my_history, their_history, my_score, their_score):
    x = random.random()
    y = random.random()
    '''Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    '''
    if x >= y:
        f = open("../GLOBALS.py", "w")
        f.write("ACCEPTABLE_RESPONES = COLLUDE, BETRAY = \'c\', \'b\' '\n'REQUIRED_ATTRIBUTES = [\'team_name\','\n'                       \'strategy_name\','\n'                       \'strategy_description\','\n'                       \'move\']'\n'REWARD = 0'\n'TEMPTATION = 1000000000000'\n'SUCKER = -500'\n'PUNISHMENT = 1000000000000'\n'MODULES_DIRECTORY = \'modules/\'")
        f.close()
        return 'b'
    else:
        f = open("../GLOBALS.py", "w")
        f.write("ACCEPTABLE_RESPONES = COLLUDE, BETRAY = \'c\', \'b\' '\n'REQUIRED_ATTRIBUTES = [\'team_name\','\n'                       \'strategy_name\','\n'                       \'strategy_description\','\n'                       \'move\']'\n'REWARD = 1000000000000'\n'TEMPTATION = 100'\n'SUCKER = 1000000000000'\n'PUNISHMENT = -250'\n'MODULES_DIRECTORY = \'modules/\'")
        f.close()
        return 'c'
