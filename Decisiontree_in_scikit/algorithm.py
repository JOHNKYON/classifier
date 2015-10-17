# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import logging
import pydot


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(msecs)05.1f pid:%(process)d [%(levelname)s] (%(funcName)s) %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='rec_posCluster.log',
    filemode='a+')
log = logging.getLogger()

log.info("Process start...")

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

# 读取iris库中数据
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)