def win():
    from third.proccess import octofinal, penalty, overtime, quater_fill, semi_fill, final
    from collections import Counter
    from itertools import combinations
    import random

    def gen_random(stage='group'):
        # function for generating random number of goals

        probs = {0: 25, 1: 55, 2: 80, 3: 90, 4: 97, 5: 99, 6: 100}
        res1 = int(random.uniform(0, 100))
        res2 = int(random.uniform(0, 100))
        for i in range(7):
            if probs[i] > res1:
                res1 = i
                break
        for i in range(7):
            if probs[i] > res2:
                res2 = i
                break

        if (stage == 'playoff') and (res1 == res2):
            res1, res2 = overtime(res1, res2)

            if res1 == res2:
                res1, res2 = penalty(res1, res2)

        return res1, res2

    def check_if_finished(group, match, result):
        # check if match finished

        match1 = match
        match2 = (match[1], match[0])
        if match1 in matches['finished'][group]:
            return True, matches['finished'][group][match1]
        elif match2 in matches['finished'][group]:
            return True, (matches['finished'][group][match2][1], matches['finished'][group][match2][0])
        return False, match

    def cal_points(teams, score, table):
        # calculate points and sum goals

        points_1 = table[teams[0]][0]
        points_2 = table[teams[1]][0]
        diff_1 = table[teams[0]][1]
        diff_2 = table[teams[1]][1]
        goals_1 = table[teams[0]][2]
        goals_2 = table[teams[1]][2]

        if score[1] > score[0]:
            return (points_1 + 0, diff_1 + score[0] - score[1], score[0] + goals_1), \
                   (points_2 + 3, diff_2 + score[1] - score[0], score[1] + goals_2)
        elif score[1] < score[0]:
            return (points_1 + 3, diff_1 + score[0] - score[1], score[0] + goals_1), \
                   (points_2 + 0, diff_2 + score[1] - score[0], score[1] + goals_2)
        else:
            return (points_1 + 1, diff_1 + score[0] - score[1], score[0] + goals_1), \
                   (points_2 + 1, diff_2 + score[1] - score[0], score[1] + goals_2)

    def cal_places(res):

        result_table = dict()
        third_place_table = dict()

        for i in res:
            result_table[i] = dict()
            temp = Counter(res[i])
            for j in range(2):
                result_table[i][j + 1] = temp.most_common(2)[j][0]
            third_place_table[temp.most_common(3)[2][0]] = (temp.most_common(3)[2][1], i)

        temp = Counter(third_place_table)
        for team in temp.most_common(4):
            result_table[team[1][1]][3] = team[0]

        return result_table

    def cal_playoffs(euro, stage):
        for i, item in enumerate(euro['playoff'][stage]):
            for j in euro['playoff'][stage][i + 1]:
                euro['playoff'][stage][i + 1][j] = gen_random(stage='playoff')

        if stage == '1/8':
            return quater_fill(euro)
        elif stage == '1/4':
            return semi_fill(euro)
        elif stage == '1/2':
            return final(euro)
        return euro

        # default dictionary

    euro = {'group':
                {'A': {},
                 'B': {},
                 'C': {},
                 'D': {},
                 'E': {},
                 'F': {}},
            'playoff': {'1/8': {},
                        '1/4': {},
                        '1/2': {},
                        'final': {},
                        'third': {}}}

    # finished matches

    matches = {'finished': {
        'A': {('FRA', 'ROU'): (2, 1), ('ALB', 'SWI'): (0, 1), ('ROU', 'SWI'): (1, 1), ('FRA', 'ALB'): (2, 0),('ALB', 'ROU'): (1, 0), ('FRA', 'SWI'): (0, 0)},
        'B': {('WAL', 'SVK'): (2, 1), ('RUS', 'SVK'): (1, 2), ('ENG', 'RUS'): (1, 1), ('ENG', 'WAL'): (2, 1), ('ENG', 'SVK'): (0, 0), ('RUS', 'WAL'): (0, 3)},
        'C': {('POL', 'NIR'): (1, 0), ('GER', 'UKR'): (2, 0), ('UKR', 'NIR'): (0, 2), ('POL', 'GER'): (0, 0), ('UKR', 'POL'): (0, 1), ('NIR', 'GER'): (0, 1)},
        'D': {('TUR', 'CRO'): (0, 1), ('ESP', 'CZE'): (1, 0), ('CZE', 'CRO'): (2, 2), ('ESP', 'TUR'): (3, 0)},
        'E': {('IRL', 'SWE'): (1, 1), ('BEL', 'ITA'): (0, 2), ('ITA', 'SWE'): (1, 0), ('BEL', 'IRL'): (3, 0)},
        'F': {('HUN', 'AUT'): (2, 0), ('POR', 'ISL'): (1, 1), ('HUN', 'ISL'): (1, 1), ('POR', 'AUT'): (0, 0)}}}

    # default groups
    groups = {
        'A': {
            'FRA': 'France',
            'SWI': 'Switzerland',
            'ROU': 'Romania',
            'ALB': 'Albania'},
        'B': {
            'ENG': 'England',
            'WAL': 'Wales',
            'SVK': 'Slovakia',
            'RUS': 'Russia'},
        'C': {
            'GER': 'Germany',
            'POL': 'Poland',
            'NIR': 'Northern Ireland',
            'UKR': 'Ukraine'},
        'D': {
            'ESP': 'Spain',
            'CRO': 'Croatia',
            'CZE': 'Czech Republic',
            'TUR': 'Turkey'},
        'E': {
            'ITA': 'Italy',
            'IRL': 'Republic of Ireland',
            'SWE': 'Sweden',
            'BEL': 'Belgium'},
        'F': {
            'HUN': 'Hungary',
            'ISL': 'Iceland',
            'POR': 'Portugal',
            'AUT': 'Austria'}}

    # generate pairs

    pairs = dict()
    for item, values in groups.iteritems():
        pairs[item] = dict()
        for pair in combinations(values.keys(), 2):
            pairs[item][pair] = tuple()

    # random.seed(2)
    # predict matches results
    for group in euro['group']:
        for match in pairs[group]:
            boo, temp_score = check_if_finished(group, match, matches['finished'][group])
            if boo:
                euro['group'][group][match] = temp_score
            else:
                euro['group'][group][match] = gen_random()

    # create dictionary with points

    points = groups.copy()

    for group in points:
        for team in points[group]:
            points[group][team] = (0, 0, 0)

            # calculate points for all groups

    for group in euro['group']:
        for match in euro['group'][group]:
            points[group][match[0]], points[group][match[1]] = cal_points(match, euro['group'][group][match],
                                                                          points[group])

    # calculate places

    results = cal_places(points)

    # generate playoff pairs

    euro = octofinal(euro, results)

    # write playoff stages
    playoff_stages = ['1/8', '1/4', '1/2', 'final', 'third']

    # generate playoff matches
    for stage in playoff_stages:
        euro = cal_playoffs(euro, stage)

    if euro['playoff']['final'][1][euro['playoff']['final'][1].keys()[0]][0] > euro['playoff']['final'][1][euro['playoff']['final'][1].keys()[0]][1]:
        return euro['playoff']['final'][1].keys()[0][0]
    return euro['playoff']['final'][1].keys()[0][1]

from collections import Counter
for j in range(5):
    winners = Counter()
    for i in range(10000):
        winners[win()] += 1

    print winners.most_common(10)
