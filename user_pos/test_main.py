# -*- coding: utf-8 -*-

from __future__ import division
import algorithm

# algorithm.run_decision_tree()

TP = 0
FP = 0
TN = 0
FN = 0

for index in range(0, 500):
    print index
    result = algorithm.run_random_forest()
    TP += result[0]
    FP += result[1]
    TN += result[2]
    FN += result[3]

precision = TP / (TP + FP)
recall = TP / (TP + FN)
accuracy = (TP + TN) / (TP+FP+TN+FN)

print("precision = %f\nrecall = %f\naccuracy = %f" % (precision, recall, accuracy))
