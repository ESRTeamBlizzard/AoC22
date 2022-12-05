symbol_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

# for part 1
outcome_map = {
    (1, 1): 3,
    (1, 2): 6,
    (1, 3): 0,
    (2, 1): 0,
    (2, 2): 3,
    (2, 3): 6,
    (3, 1): 6,
    (3, 2): 0,
    (3, 3): 3,
}

# for part 2
choice_map = {
    (1, 1): 3,
    (1, 2): 1,
    (1, 3): 2,
    (2, 1): 1,
    (2, 2): 2,
    (2, 3): 3,
    (3, 1): 2,
    (3, 2): 3,
    (3, 3): 1,
}

with open('input/2.txt', mode='rt') as f:
    total_score = 0

    for line in f:
        opp_move = symbol_map[line[0]]

        # part 1
        my_move = symbol_map[line[2]]

        # part 2
        # outcome = symbol_map[line[2]]
        # my_move = choice_map[opp_move, outcome]

        # score for my choice
        total_score += my_move

        # score for outcome
        total_score += outcome_map[(opp_move, my_move)]

print(total_score)
