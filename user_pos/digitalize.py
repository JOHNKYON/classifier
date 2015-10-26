# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import json
import codecs

# 建立评分细则

# 第一阶段可直接数字化的项有 7是否接受调剂 8婚姻状况 海外经历
# 政治面貌 亲友关系 实习与否 是否报考硕博 学校级别(读json) 学历 学位
# 年级排名 获奖级别 英语等级 期望月薪（留议)


# 打开输入文件
input_people = codecs.open("./data_under_doing/employer", 'r', encoding='utf-8')
output_people = codecs.open("./data_under_doing/employer_digital", 'w', encoding='utf-8')
label_file = codecs.open("./data_under_doing/label_employed", 'r', encoding='utf-8')


# 一次性读取label文件
label = json.loads(label_file.read(), encoding='utf-8')

# 逐步数字化
for line in input_people.readlines():
    person_digital = dict()
    person = json.loads(line)
    if person[label["7"]] == "是":
        person_digital["7"] = "1"
    else:
        person_digital["7"] = "0"


# 评分

# 储存评分内容


# 关闭打开的文件
input_people.close()
output_people.close()
label_file.close()
