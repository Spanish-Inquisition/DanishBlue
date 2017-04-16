####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'fTfT'
strategy_name = 'Forgiving Collude but retaliate'
strategy_description = '''\
Collude first round. Collude, except in a round after getting 
a severe punishment. After 3 double betrays, colludes.'''
    
def move(my_history, their_history, my_score, their_score):

    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif len(my_history) >=3 and my_history[-1] + my_history[-2] + my_history[-3] == 'bbb':
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.