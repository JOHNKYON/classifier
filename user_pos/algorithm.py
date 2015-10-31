# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import log_conf
import data
# import conf
import numpy
import codecs
import json

from sklearn import tree
from sklearn.externals.six import StringIO


def run():
    # 开始运行
    log_conf.logger.info("user_pos matching starting...")

    log_conf.logger.info("Training star...")

    # 打开输入文件
    input_employer = codecs.open("./data_under_doing/employer_digital", 'r', encoding='utf-8')
    input_loser = codecs.open("./data_under_doing/loser_digital", 'r', encoding='utf-8')

    training = list()

    count = 0
    # 读90个录取员工作为训练
    lines = input_employer.readlines()
    for line in lines:
        if count == 90:
            break

        person = json.loads(line)
        person_list = [person["7"], person["8"], person["9"], person["10"], person["11"], person["12"], person["13"],
                       person["15"], person["17"], person["23"]]

        training.append(person_list)

        count += 1

    # 读500个落选者作为训练
    count = 0
    for line in input_loser.readlines():
        if count == 500:
            break

        person = json.loads(line)
        person_list = [person["6"], person["7"], person["8"], person["9"], person["10"], person["11"], person["12"],
                       person["14"], person["16"], person["22"]]

        training.append(person_list)

        count += 1

    # 生成训练集Numpy array
    x = numpy.array(training)

    # 生成标签
    label_temp = numpy.array([1, 0])
    y = label_temp.repeat([90, 500])

    clf = tree.DecisionTreeClassifier()
    clf.fit(x, y)

    # 输出决策树图像
    with open("tree.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

    test_employer = list()
    # 测试树的决策性能
    count = 0
    test_count = 0
    for line in lines:
        if count <= 90:
            person = json.loads(line)
            person_list = [person["7"], person["8"], person["9"], person["10"], person["11"], person["12"], person["13"],
                       person["15"], person["17"], person["23"]]

            if clf.predict(person_list)[0] == 1:
                test_count += 1

        else:
            if count > 140:
                break
            count += 1
            continue

        count += 1

    print test_count/90
    # 关闭输入文件
    input_employer.close()
    input_loser.close()
