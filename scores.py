#!/usr/bin/env python

scores = {}

with open('DATA/testscores.dat') as scores_in:
    for line in scores_in:
        student, raw_score = line.split(':')
        score = int(raw_score)
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
        scores[student] = score, letter_grade

score_total = 0
for name, data in sorted(scores.items()):
    score_total += data[0]
    print("{:20s} {:2d} {}".format(name, data[0], data[1]))

average = score_total / len(scores)
print("Average score: {:.2f}".format(average))


