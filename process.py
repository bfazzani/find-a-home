def calculateScore(prefs, info):
    score = 0
    for i, j in zip(prefs, info):
        score += i*j
    return score / len(prefs)
