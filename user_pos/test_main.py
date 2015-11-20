# -*- coding: utf-8 -*-

from __future__ import division
import algorithm

# algorithm.run_decision_tree()

TP = 0
FP = 0
TN = 0
FN = 0

small = 150
big = 170

'''
def pre_small(para):
    init_TP_small = 0
    init_FP_small = 0
    init_TN_small = 0
    init_FN_small = 0
    print para
    for index in range(0, 500):
        init_small = algorithm.run_random_forest(para)
        init_TP_small += init_small[0]
        init_FP_small += init_small[1]
        init_TN_small += init_small[2]
        init_FN_small += init_small[3]
    small_pre = init_TP_small/(init_TP_small+init_FP_small)
    return small_pre


def pre_big(para):
    init_TP_big = 0
    init_FP_big = 0
    init_TN_big = 0
    init_FN_big = 0
    print para
    for index in range(0, 500):
        init_big = algorithm.run_random_forest(170)
        init_TP_big += init_big[0]
        init_FP_big += init_big[0]
        init_TN_big += init_big[0]
        init_FN_big += init_big[0]
    big_pre = init_TP_big/(init_TP_big+init_FP_big)
    return big_pre


while small != big and small != big-1:
    small_pre = pre_small(small)
    big_pre = pre_big(big)
    if small_pre > big_pre:
        big = round((small+big)/2)
    else:
        small = round((small+big)/2)


print("small\t"+str(small))
print("big\t"+str(big))

print pre_small(small)
print pre_big(big)'''

muilt = 1

'''while muilt:
    try:
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for index in range(0, 1000):
            print index
            result = algorithm.run_random_forest(90*muilt)
            TP += result[0]
            FP += result[1]
            TN += result[2]
            FN += result[3]

        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        accuracy = (TP + TN) / (TP + FP + TN + FN)
        muilt += 0.2
    except:
        print muilt
        break'''
for index in range(0, 500):
    print index
    result = algorithm.run_random_forest(1800)
    TP += result[0]
    FP += result[1]
    TN += result[2]
    FN += result[3]

precision = TP / (TP + FP)
recall = TP / (TP + FN)
accuracy = (TP + TN) / (TP + FP + TN + FN)

print("precision = %f\nrecall = %f\naccuracy = %f" % (precision, recall, accuracy))
