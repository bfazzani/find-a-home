def calculateScore(prefs, info):
    score = 0
    for i, j in zip(prefs, info):
        score += i*j
    return score / len(prefs)

print(calculateScore((80, 40, 90), (3, 2, 5)))
