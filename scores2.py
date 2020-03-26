#!/usr/bin/env python



def get_grade(score):
    if score > 94:
        letter_grade = 'A'
    elif score > 88:
        letter_grade = 'B'
    elif score > 82:
        letter_grade = 'C'
    elif score > 74:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade

scores = {}

with open('DATA/testscores.dat') as scores_in:
    for line in scores_in:
        student, score = line.split(':')
        scores[student] = int(score)

score_total = 0
for name, score in sorted(scores.items()):
    letter_grade = get_grade(score)
    score_total += score
    print("{:20s} {:2d} {}".format(name, score, letter_grade))

average = score_total / len(scores)
print("Average score: {:.2f}".format(average))


