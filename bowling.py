def calc_score(rounds):
    total_score = 0
    rounds = rounds.replace(" ", "")
    for score in rounds:
        if score != "X":
            total_score += int(score)
        else:
            total_score += 10
    return total_score