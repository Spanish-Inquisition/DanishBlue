'''
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
'''

import GLOBALS
from teamclass import Team
from pandas import DataFrame
import random

default_module_names = ['examplemodules/example0.py',
                        'examplemodules/example1.py',
                        'examplemodules/example2.py',
                        'examplemodules/example3.py']


def sum_list(list_to_sum):
    '''
    I feel like this function is pretty intuitive
    given a list of numbers, it adds them together
    '''
    count = 0
    for value in list_to_sum:
        count += value
    return count


def load_modules(module_names):
    '''
    Given a list of strings with paths to modules,
    load them. Return a list of teams, which are
    instances of Team from teamclass.py
    '''
    teams = [False] * len(module_names)
    for count in range(len(module_names)):
        teams[count] = Team(module_names[count])
    assert False not in teams
    return teams


def play_tournament(modules):
    scores = [[False for i in range(len(modules))] for j in range(len(modules))]  # an n*n list for scores
    # each player's scores are in scores[that_player][opponent]
    moves = [[False for i in range(len(modules))] for j in range(len(modules))]  # an n*n list for moves
    for first_team_index in range(len(modules)):
        for second_team_index in range(first_team_index + 1):
            # each player plays against all the players before them
            if first_team_index == second_team_index:
                # if you're playing yourself, score 0 and make no moves
                scores[first_team_index][first_team_index] = 0
                moves[first_team_index][first_team_index] = ''
            else:
                # play against the opponent, log scores in the lists
                player_1 = modules[first_team_index]
                player_2 = modules[second_team_index]
                player_1_score, player_2_score, player_1_moves, player_2_moves = play_round(player_1, player_2)
                scores[first_team_index][second_team_index] = player_1_score
                scores[second_team_index][first_team_index] = player_2_score
                moves[first_team_index][second_team_index] = player_1_moves
                moves[second_team_index][first_team_index] = player_2_moves
    return scores, moves


def play_round(player_1, player_2):
    NUMBER_OF_ROUNDS = random.randint(100, 200)
    player_1_moves = ''
    player_2_moves = ''
    player_1_score = 0
    player_2_score = 0
    for round in range(NUMBER_OF_ROUNDS):
        player_1_single_score, \
            player_2_single_score, \
            player_1_single_move, \
            player_2_single_move \
            = play_single_dilemma(player_1,
                                  player_2,
                                  player_1_score,
                                  player_2_score,
                                  player_1_moves,
                                  player_2_moves)
        player_1_score += player_1_single_score
        player_2_score += player_2_single_score
        player_1_moves += player_1_single_move
        player_2_moves += player_2_single_move
    player_1_score = int(player_1_score / NUMBER_OF_ROUNDS)
    player_2_score = int(player_2_score / NUMBER_OF_ROUNDS)
    return player_1_score, player_2_score, player_1_moves, player_2_moves


def play_single_dilemma(player_1,
                        player_2,
                        player_1_score,
                        player_2_score,
                        player_1_moves,
                        player_2_moves):

    player_1_move = player_1.move(player_1_moves,
                                  player_2_moves,
                                  player_1_score,
                                  player_2_score)
    player_2_move = player_2.move(player_2_moves,
                                  player_1_moves,
                                  player_2_score,
                                  player_1_score)
    assert type(player_1_move) is str
    assert type(player_2_move) is str
    assert player_1_move in GLOBALS.ACCEPTABLE_RESPONES
    assert player_2_move in GLOBALS.ACCEPTABLE_RESPONES
    player_1_round_score = 0
    player_2_round_score = 0
    if (player_1_move == 'c') and (player_2_move == 'c'):
        player_1_round_score += GLOBALS.REWARD
        player_2_round_score += GLOBALS.REWARD
    elif (player_1_move == 'c') and (player_2_move == 'b'):
        player_1_round_score += GLOBALS.SUCKER
        player_2_round_score += GLOBALS.TEMPTATION
    elif (player_1_move == 'b') and (player_2_move == 'c'):
        player_1_round_score += GLOBALS.TEMPTATION
        player_2_round_score += GLOBALS.SUCKER
    elif (player_1_move == 'b') and (player_2_move == 'b'):
        player_1_round_score += GLOBALS.PUNISHMENT
        player_2_round_score += GLOBALS.PUNISHMENT
    return player_1_round_score,\
        player_2_round_score,\
        player_1_move,\
        player_2_move


def make_section_title(title):
    print('{:-^80}'.format(''))
    print('{:^80}'.format(title))
    print('{:-^80}'.format(''))


def make_single_team_section_0(team, count):
    print('P{0}: {1} using {2} ({3})'.format(count, team.team_name, team.strategy_name, team.strategy_description))


def make_section_0(teams):
    make_section_title('Lineup')
    for team_number in range(len(teams)):
        teams[team_number].team_number = team_number
        make_single_team_section_0(teams[team_number], team_number)


def make_section_1(teams, scores):
    make_section_title('Player vs. Player Scores')
    print('To find player n\'s average score against player m, check the nth row and the mth column')
    print(DataFrame(scores))


def make_section_2(teams, scores):
    make_section_title('Standings')
    for team_index in range(len(teams)):
        teams[team_index].summed_scores = sum_list(scores[team_index])
    teams.sort(key=lambda team: team.summed_scores, reverse=True)
    for team_index in range(len(teams)):
        team = teams[team_index]
        print('{0:2}) {1:<16}(P{2}): {3:>8} points with {4:<20}'.format(team_index + 1, team.team_name, team.team_number, team.summed_scores, team.strategy_name))


def main(module_names):
    teams = load_modules(module_names)
    if not teams:
        return 1
    else:
        make_section_0(teams)
        scores, moves = play_tournament(teams)
        make_section_1(teams, scores)
        make_section_2(teams, scores)
