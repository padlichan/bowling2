def calc_score(rounds):
    total_score = 0
    rounds = rounds.replace(" ", "")
    for score in rounds:
        total_score += int(score)
    return total_score