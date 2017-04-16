####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DanishBlue'
strategy_name = 'Mozarella Factory'
strategy_description = '''\
Run the whole tournament with various algorithms, and pick the best one.'''



def move(my_history, their_history, my_score, their_score, chosen):

    if their_history[0:6] == 'cbccbc':
        if len(my_history) == 6:
            return 'c'
        elif len(my_history) == 7:
            return 'c'
        elif len(my_history) == 8:
            return 'b'
        elif len(my_history) == 9:
            return 'b'
        else:
            return 'b'
    else:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
