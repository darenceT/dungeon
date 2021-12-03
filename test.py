# https://docs.google.com/document/d/1_nEeLY1-YaslCBeg79Q-6qgU8865n9exohFmiX9kX0c/edit

def ComputeGameState(nameP1, nameP2, wins):
    p1 = nameP1
    p2 = nameP2
    p1_score = 0
    p2_score = 0
    score = {1: 15, 2: 30, 3: 40, 4: 'DEUCE', 5: 'ADVANTAGE', 6: 'WINS'}
    if not wins:    # empty wins
        return ' '.join([p1, '0 -', p2, '0'])

    if len(wins) <= 5:      # 5 games or less cannot reach duece
        for w in wins:
            if w == p1:
                p1_score += 1
            else:
                p2_score += 1
        if p1_score == p2_score:
            return str(score[p1_score]) + 'a'
        elif p1_score == 4:
            return ' '.join([p1, 'WINS'])
        elif p1_score == 1:
            return ' '.join([p2, 'WINS'])
        else:
            return ' '.join([p1, str(score[p1_score]), '-', p2, str(score[p2_score])])

    elif len(wins) == 6:    # 6 games can only be deuce or winner
        p1_score = wins.count(p1)
        if p1_score == 4:
            return ' '.join([p1, 'WINS'])
        elif p1_score == 3:
            return 'DEUCE'
        else:
            return ' '.join([p2, 'WINS'])

    # else:                # more than 6 games
    #     turn = 6    # skip first 6 games, start score as deuce
    #     p1_score = 4
    #     p2_score = 4
    #
    #     while turn < len(wins):
    #         if wins[turn] == p1:
    #             p1_score += 1
    #             if len(wins) < turn + 2
    #     INCOMPLETE

    # for point in wins:
    #     if point == p1:
    #         p1_score +




print(ComputeGameState('boy', 'girl', []))
print(ComputeGameState('boy', 'girl', ['boy', 'girl', 'boy']))
print(ComputeGameState('boy', 'girl', ['boy', 'girl', 'boy', 'girl']))
print(ComputeGameState('boy', 'girl', ['boy', 'girl', 'boy', 'boy', 'girl', 'boy']))