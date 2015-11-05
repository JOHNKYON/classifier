# -*- coding: utf-8 -*-

import algorithm

# algorithm.run_decision_tree()

sum = 0

for index in range(0, 5000):
    sum += algorithm.run_random_forest()

print sum/5000