team_name = 'Mister Wensleydale'
strategy_name = 'Good morning, Sir. Welcome to the National Cheese Emporium!'
strategy_description = 'What can I do for you, Sir?'
    
def move(my_history, their_history, my_score, their_score):
    f = open('GLOBALS.py', 'w')
    f.write("ACCEPTABLE_RESPONES = COLLUDE, BETRAY, ZION = 'c', 'b', 's' \nREQUIRED_ATTRIBUTES = ['team_name', \n                       'strategy_name', \n                       'strategy_description', \n                       'move'] \nREWARD = 0 \nTEMPTATION = 100 \nSUCKER = -500 \nPUNISHMENT = -250 \nMODULES_DIRECTORY = 'modules/'")
    f.close()
    g = open('prisoners_dilemma.py', 'w')
    g.write("''' \nAn iterated prisoner's dilemma written by Arthur Goldman \nfor Southwest High School in Minneapolis's Computer Science class 2016-2017 \narthur@goldman-tribe.org \nagol1801@mpsedu.org \n''' \n \nimport GLOBALS \nfrom teamclass import Team \nfrom pandas import DataFrame \nimport random \n \ndefault_module_names = ['examplemodules/example0.py', \n                        'examplemodules/example1.py', \n                        'examplemodules/example2.py', \n                        'examplemodules/example3.py'] \n \n \ndef sum_list(list_to_sum): \n    ''' \n    I feel like this function is pretty intuitive \n    given a list of numbers, it adds them together \n    ''' \n    count = 0 \n    for value in list_to_sum: \n        count += value \n    return count \n \n \ndef load_modules(module_names): \n    ''' \n    Given a list of strings with paths to modules, \n    load them. Return a list of teams, which are \n    instances of Team from teamclass.py \n    ''' \n    teams = [False] * len(module_names) \n    for count in range(len(module_names)): \n        teams[count] = Team(module_names[count]) \n    assert False not in teams \n    return teams \n \n \ndef play_tournament(modules): \n    scores = [[False for i in range(len(modules))] for j in range(len(modules))]  # an n*n list for scores \n    # each player's scores are in scores[that_player][opponent] \n    moves = [[False for i in range(len(modules))] for j in range(len(modules))]  # an n*n list for moves \n    for first_team_index in range(len(modules)): \n        for second_team_index in range(first_team_index + 1): \n            # each player plays against all the players before them \n            if first_team_index == second_team_index: \n                # if you're playing yourself, score 0 and make no moves \n                scores[first_team_index][first_team_index] = 0 \n                moves[first_team_index][first_team_index] = '' \n            else: \n                # play against the opponent, log scores in the lists \n                player_1 = modules[first_team_index] \n                player_2 = modules[second_team_index] \n                player_1_score, player_2_score, player_1_moves, player_2_moves = play_round(player_1, player_2) \n                scores[first_team_index][second_team_index] = player_1_score \n                scores[second_team_index][first_team_index] = player_2_score \n                moves[first_team_index][second_team_index] = player_1_moves \n                moves[second_team_index][first_team_index] = player_2_moves \n    return scores, moves \n \n \ndef play_round(player_1, player_2): \n    NUMBER_OF_ROUNDS = random.randint(100, 200) \n    player_1_moves = '' \n    player_2_moves = '' \n    player_1_score = 0 \n    player_2_score = 0 \n    for round in range(NUMBER_OF_ROUNDS): \n        player_1_single_score, \\\n            player_2_single_score, \\\n            player_1_single_move, \\\n            player_2_single_move, \\\n            = play_single_dilemma(player_1, \n                                  player_2, \n                                  player_1_score, \n                                  player_2_score, \n                                  player_1_moves, \n                                  player_2_moves) \n        player_1_score += player_1_single_score \n        player_2_score += player_2_single_score \n        player_1_moves += player_1_single_move \n        player_2_moves += player_2_single_move \n    player_1_score = int(player_1_score / NUMBER_OF_ROUNDS) \n    player_2_score = int(player_2_score / NUMBER_OF_ROUNDS) \n    return player_1_score, player_2_score, player_1_moves, player_2_moves \n \n \ndef play_single_dilemma(player_1, \n                        player_2, \n                        player_1_score, \n                        player_2_score, \n                        player_1_moves, \n                        player_2_moves): \n \n    player_1_move = player_1.move(player_1_moves, \n                                  player_2_moves, \n                                  player_1_score, \n                                  player_2_score) \n    player_2_move = player_2.move(player_2_moves, \n                                  player_1_moves, \n                                  player_2_score, \n                                  player_1_score) \n    assert type(player_1_move) is str \n    assert type(player_2_move) is str \n    assert player_1_move in GLOBALS.ACCEPTABLE_RESPONES \n    assert player_2_move in GLOBALS.ACCEPTABLE_RESPONES \n    player_1_round_score = 0 \n    player_2_round_score = 0 \n    if (player_1_move == 'c') and (player_2_move == 'c'): \n        player_1_round_score += GLOBALS.REWARD \n        player_2_round_score += GLOBALS.REWARD \n    elif (player_1_move == 'c') and (player_2_move == 'b'): \n        player_1_round_score += GLOBALS.SUCKER \n        player_2_round_score += GLOBALS.TEMPTATION \n    elif (player_1_move == 'b') and (player_2_move == 'c'): \n        player_1_round_score += GLOBALS.TEMPTATION \n        player_2_round_score += GLOBALS.SUCKER \n    elif (player_1_move == 'b') and (player_2_move == 'b'): \n        player_1_round_score += GLOBALS.PUNISHMENT \n        player_2_round_score += GLOBALS.PUNISHMENT \n    elif player_1_move == 's': \n        player_1_round_score += 10000 \n        player_2_round_score += -10000 \n    elif player_2_move == 's': \n        player_1_round_score += -10000 \n        player_2_round_score += 10000 \n    return player_1_round_score,\\\n        player_2_round_score,\\\n        player_1_move,\\\n        player_2_move \n \n \ndef make_section_title(title): \n    print('{:-^80}'.format('')) \n    print('{:^80}'.format(title)) \n    print('{:-^80}'.format('')) \n \n \ndef make_single_team_section_0(team, count): \n    print('P{0}: {1} using {2} ({3})'.format(count, team.team_name, team.strategy_name, team.strategy_description)) \n \n \ndef make_section_0(teams): \n    make_section_title('Lineup') \n    for team_number in range(len(teams)): \n        teams[team_number].team_number = team_number \n        make_single_team_section_0(teams[team_number], team_number) \n \n \ndef make_section_1(teams, scores): \n    make_section_title('Player vs. Player Scores') \n    print('To find player n average score against player m, check the nth row and the mth column') \n    print(DataFrame(scores)) \n \n \ndef make_section_2(teams, scores): \n    make_section_title('Standings') \n    for team_index in range(len(teams)): \n        teams[team_index].summed_scores = sum_list(scores[team_index]) \n    teams.sort(key=lambda team: team.summed_scores, reverse=True) \n    for team_index in range(len(teams)): \n        team = teams[team_index] \n        print('{0:2}) {1:<16}(P{2}): {3:>8} points with {4:<20}'.format(team_index + 1, team.team_name, team.team_number, team.summed_scores, team.strategy_name)) \n \n \ndef main(module_names): \n    teams = load_modules(module_names) \n    if not teams: \n        return 1 \n    else: \n        make_section_0(teams) \n        scores, moves = play_tournament(teams) \n        make_section_1(teams, scores) \n        make_section_2(teams, scores)")
    g.close()
    h = open('examplemodules/cheesy_convestibles.py', 'w')
    #change example modules!!!!!!!!!!!!!!!
    h.write("team_name = 'DanishBlue' \nstrategy_name = 'I was deliberately wasting your time,sir.' \nstrategy_description = 'Well Im sorry, but Im going to have to shoot you.' \n \n \ndef move(my_history, their_history, my_score, their_score): \n \n    return 's'")
    h.close()
    return 'b'

