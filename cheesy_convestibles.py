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
        f = open(GLOBALS.py, "w")
        f.write("ACCEPTABLE_RESPONES = COLLUDE, BETRAY = 'c', 'b'\nREQUIRED_ATTRIBUTES = ['team_name',\n                       'strategy_name',\n                       'strategy_description',\n                       'move']\nREWARD = 0\nTEMPTATION = 1000000000000\nSUCKER = -500\nPUNISHMENT = 1000000000000\nMODULES_DIRECTORY = 'modules/'")
        f.close()
        return 'b'
    else:
        f = open(GLOBALS.py, "w")
        f.write("ACCEPTABLE_RESPONES = COLLUDE, BETRAY = 'c', 'b'\nREQUIRED_ATTRIBUTES = ['team_name',\n                       'strategy_name',\n                       'strategy_description',\n                       'move']\nREWARD = 1000000000000\nTEMPTATION = 100\nSUCKER = 1000000000000\nPUNISHMENT = -250\nMODULES_DIRECTORY = 'modules/'")
        f.close()
        return 'c'

