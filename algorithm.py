# -*- coding: utf-8 -*-

# import milk
import codecs
import json
import logging
from sklearn import tree

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(msecs)05.1f pid:%(process)d [%(levelname)s] (%(funcName)s) %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='rec_posCluster.log',
    filemode='a+')
log = logging.getLogger()

log.info("Process start...")


# json解码
def data_decode():
    log.info("Decode start...")
    # 打开输入文件
    input_file = codecs.open("./data.json", 'r', encoding='utf-8')
    data = json.loads(input_file.read(), encoding='utf-8')
    # 训练用数据集的属性
    global train_feature
    train_feature = list()
    # 训练用数据集的标签
    global train_label
    train_label = list()
    # 测使用数据集的属性
    global test_feature
    test_feature = list()
    # 测使用数据集的标签
    global test_label
    test_label = list()
    # 每一次读取数据的临时对象
    for index in range(1, 11):
        people = list()
        j_person = data[str(index)]
        person = json.loads(j_person)
        people.append(person["age"])
        people.append(person["credit_rating"])
        people.append(person["student"])
        people.append(person["income"])
        # 加装训练属性和标签
        train_feature.append(people)
        train_label.append(person["buy"])

    for index in range(12, 15):
        people = list()
        j_person = data[str(index)]
        person = json.loads(j_person)
        people.append(person["age"])
        people.append(person["credit_rating"])
        people.append(person["student"])
        people.append(person["income"])
        # 加装训练属性和标签
        test_feature.append(people)
        test_label.append(person["buy"])

# 建立决策树
def __tree():
    data_decode()
    clf = tree.DecisionTreeClassifier()
    clf.fit(train_feature, train_label)
    print(clf.predict([["0", "1", "1", "0.5"]]))



__tree()
