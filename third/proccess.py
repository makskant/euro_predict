# -*- coding: utf-8 -*-
"""

@author: vitaliyradchenko
"""

def octofinal(euro, results):
    euro['playoff']['1/8'][1]={(results['A'][2], results['C'][2]):(0,0)}
    euro['playoff']['1/8'][6]={(results['F'][1], results['E'][2]):(0,0)}
    euro['playoff']['1/8'][7]={(results['E'][1], results['D'][2]):(0,0)}
    euro['playoff']['1/8'][8]={(results['B'][2], results['F'][2]):(0,0)}
    if (3 in results['A'].keys()) and (3 in results['B'].keys()) and (3 in results['C'].keys()) and (3 in results['D'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['B'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['A'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['B'].keys()) and (3 in results['C'].keys()) and (3 in results['E'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['B'].keys()) and (3 in results['C'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['B'].keys()) and (3 in results['D'].keys()) and (3 in results['E'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['B'].keys()) and (3 in results['D'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['B'].keys()) and (3 in results['E'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['C'].keys()) and (3 in results['D'].keys()) and (3 in results['E'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['A'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['C'].keys()) and (3 in results['D'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['A'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['C'].keys()) and (3 in results['E'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['F'][3]): (0, 0)}
    elif (3 in results['A'].keys()) and (3 in results['D'].keys()) and (3 in results['E'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['A'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['F'][3]): (0, 0)}
    elif (3 in results['B'].keys()) and (3 in results['C'].keys()) and (3 in results['D'].keys()) and (3 in results['E'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['B'].keys()) and (3 in results['C'].keys()) and (3 in results['D'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['B'].keys()) and (3 in results['C'].keys()) and (3 in results['E'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    elif (3 in results['B'].keys()) and (3 in results['D'].keys()) and (3 in results['E'].keys()) and (3 in results['F'].keys()):
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['F'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['B'][3]): (0, 0)}
    else:
        euro['playoff']['1/8'][2] = {(results['B'][1], results['D'][3]): (0, 0)}
        euro['playoff']['1/8'][3] = {(results['D'][1], results['E'][3]): (0, 0)}
        euro['playoff']['1/8'][4] = {(results['A'][1], results['C'][3]): (0, 0)}
        euro['playoff']['1/8'][5] = {(results['C'][1], results['F'][3]): (0, 0)}

    return euro


def penalty(res1, res2):
    # function generating process of penalties
    import random

    def check(score1, score2, shot):
        if (score2 + 4 - shot < score1) or (score1 + 4 - shot < score2):
            return True
        return False

    score1 = 0
    score2 = 0

    for shot in range(5):
        goal1 = int(random.uniform(0, 100))
        goal2 = int(random.uniform(0, 100))

        if goal1 > 20:
            score1 += 1

        if check(score1, score2, shot):
            return res1 + (score1,), res2 + (score2,)

        if goal2>20:
            score2 +=1

        if check(score1, score2, shot):
            return res1 + (score1,), res2 + (score2,)

    if score1 == score2:
        while score2 == score1:
            goal1 = int(random.uniform(0, 100))
            goal2 = int(random.uniform(0, 100))
            if goal1 > 20:
                score1 += 1
            if goal2 > 20:
                score2 += 1

    return res1 + (score1,), res2 + (score2,)


def overtime(score1, score2):
    import random
    probs = {0: 7, 1: 9, 2: 10}
    res1 = int(random.uniform(0, 10))
    res2 = int(random.uniform(0, 10))
    for i in range(7):
        if probs[i] > res1:
            res1 = i
            break
    for i in range(7):
        if probs[i] > res2:
            res2 = i
            break
    return (res1 + score1, res1,), (res2 + score2, res2,)


def winner(teams, result):
    if result[0] > result[1]:
        return teams[0]
    return teams[1]


def losser(teams, result):
    if result[0] > result[1]:
        return teams[1]
    return teams[0]


def quater_fill(results):
    for_quater = dict()

    for i in results['playoff']['1/8']:
        for match in results['playoff']['1/8'][i]:
            for_quater[i] = winner(match, results['playoff']['1/8'][i][match])

    for i in range(1, 5):
        results['playoff']['1/4'][i] = dict()
    results['playoff']['1/4'][1][(for_quater[1], for_quater[3])] = (0, 0)
    results['playoff']['1/4'][2][(for_quater[2], for_quater[6])] = (0, 0)
    results['playoff']['1/4'][4][(for_quater[4], for_quater[8])] = (0, 0)
    results['playoff']['1/4'][3][(for_quater[5], for_quater[7])] = (0, 0)

    return results


def semi_fill(results):
    for_semi = dict()

    for i in results['playoff']['1/4']:
        for match in results['playoff']['1/4'][i]:
            for_semi[i] = winner(match, results['playoff']['1/4'][i][match])

    for i in range(1, 3):
        results['playoff']['1/2'][i] = dict()
    results['playoff']['1/2'][1][(for_semi[1], for_semi[2])] = (0, 0)
    results['playoff']['1/2'][2][(for_semi[3], for_semi[4])] = (0, 0)
    return results


def final(results):
    for_final = dict()
    for_third = dict()

    for i in results['playoff']['1/2']:
        for match in results['playoff']['1/2'][i]:
            for_final[i] = winner(match, results['playoff']['1/2'][i][match])
            for_third[i] = losser(match, results['playoff']['1/2'][i][match])

    results['playoff']['final'][1] = dict()
    results['playoff']['third'][1] = dict()
    results['playoff']['final'][1][(for_final[1], for_final[2])] = (0, 0)
    results['playoff']['third'][1][(for_third[1], for_third[2])] = (0, 0)

    return results
