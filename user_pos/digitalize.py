# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import json
import codecs

# 建立评分细则

# 第一阶段可直接数字化的项有 7是否接受调剂 8婚姻状况 9海外经历
# 10政治面貌 11亲友关系 12实习与否 13是否报考硕博 15学校级别(读json) 学历 学位
# 年级排名 获奖级别 英语等级 期望月薪（留议)


# 打开输入文件
input_people = codecs.open("./data_under_doing/employer", 'r', encoding='utf-8')
output_people = codecs.open("./data_under_doing/employer_digital", 'w', encoding='utf-8')
label_file = codecs.open("./data_under_doing/label_employed.json", 'r', encoding='utf-8')
school_info_file = codecs.open("./data/school_info.json", 'r', encoding='utf-8')


school_info = school_info_file.readlines()


# 一次性读取label文件
label = json.loads(label_file.read(), encoding='utf-8')
# 一次性读取school_info


def find_line(str, text):
    for lines in text:
        if str in lines:
            return lines


# 逐步数字化
for line in input_people.readlines():
    person_digital = dict()
    person = json.loads(line)

    # 是否接受调剂
    if person[label["7"]] == "是":
        person_digital["7"] = 1
    else:
        person_digital["7"] = 0

    # 婚姻状况
    if person[label["8"]] == "已婚":
        person_digital["8"] = 1
    else:
        person_digital["7"] = 0

    # 海外经历
    if person[label["9"]] == "是":
        person_digital["9"] = 1
    else:
        person_digital["9"] = 0

    # 政治面貌
    if person[label["10"]] == "中共党员(含预备党员)":
        person_digital["10"] = 1
    elif person[label["10"]] == "团员":
        person_digital["10"] = 0.5
    else:
        person_digital["10"] = 0

    # 亲友关系
    if person[label["11"]] == "是":
        person_digital["11"] = 1
    else:
        person_digital["11"] = 0

    # 是否报考硕博
    if person[label["12"]] == "是":
        person_digital["11"] = 1
    else:
        person_digital["11"] = 0

    # 学校级别
    school_name = person[label["15"]]
    j_user_school = find_line(school_name, school_info)
    print j_user_school
    '''user_school = json.loads(j_user_school, encoding='utf-8')
    if user_school["is_985"]:
        person_digital["15"] = 1
    elif user_school["is_211"]:
        person_digital["15"] = 0.5
    else:
        person_digital["15"] = 0

    # 暂且存储
    j_person_digital = json.dumps(person_digital)
    output_people.write(j_person_digital)'''

# 评分

# 储存评分内容


# 关闭打开的文件
input_people.close()
output_people.close()
label_file.close()
