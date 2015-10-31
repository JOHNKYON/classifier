# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import codecs

# 建立评分细则

# 第一阶段可直接数字化的项有 6是否接受调剂 7婚姻状况 8海外经历
# 9政治面貌 10亲友关系 11实习与否 12是否报考硕博 14学校级别(读json) 16学历 17学位
# 22年级排名 获奖级别 英语等级 期望月薪（留议)


# 打开输入文件
input_people = codecs.open("./data_under_doing/loser", 'r', encoding='utf-8')
output_people = codecs.open("./data_under_doing/loser_digital", 'w', encoding='utf-8')
label_file = codecs.open("./data_under_doing/label_unemployed.json", 'r', encoding='utf-8')
school_info_file = codecs.open("./data/school_info.json", 'r', encoding='utf-8')

school_info = school_info_file.readlines()


# 一次性读取label文件
label = json.loads(label_file.read(), encoding='utf-8')


# 一次性读取school_info

# 直接返回对学校的评分
def school_digitalize(str, text):
    for lines in text:
        if str in lines:
            user_school = json.loads(lines, encoding='utf-8')
            if user_school["is_985"]:
                return 1
            elif user_school["is_211"]:
                return 0.5
            else:
                return 0

    return -0.1


# 返回对年级排名的评分
def grade_dig(str):
    if str == "Top 10%":
        return 0.8
    elif str == "Top 5%":
        return 1
    elif str == "Top 20%":
        return 0.6
    elif str == "Top 30%":
        return 0.4
    elif str == "Top 40%":
        return 0.2
    elif str == "Top 50%":
        return 0
    else:
        return -0.1

# count = 0
# 逐步数字化
for line in input_people.readlines():
    # count += 1
    person_digital = dict()
    person = json.loads(line)

    # 是否接受调剂
    if person[label["6"]] == "是":
        person_digital["6"] = 1
    else:
        person_digital["6"] = 0

    # 婚姻状况
    if person[label["7"]] == "已婚":
        person_digital["7"] = 1
    else:
        person_digital["7"] = 0

    # 海外经历
    if person[label["8"]] == "是":
        person_digital["8"] = 1
    else:
        person_digital["8"] = 0

    # 政治面貌
    if person[label["9"]] == "中共党员(含预备党员)":
        person_digital["9"] = 1
    elif person[label["9"]] == "团员":
        person_digital["9"] = 0.5
    else:
        person_digital["9"] = 0

    # 亲友关系
    if person[label["10"]] == "是":
        person_digital["10"] = 1
    else:
        person_digital["10"] = 0

    # 实习与否
    if person[label["11"]] == "是":
        person_digital["11"] = 1
    else:
        person_digital["11"] = 0

    # 是否报考硕博
    if person[label["12"]] == "是":
        person_digital["12"] = 1
    else:
        person_digital["12"] = 0

    # 学校级别
    school_name = person[label["14"]]
    person_digital["14"] = school_digitalize(school_name, school_info)

    # 学历
    if person[label["16"]] == "硕士研究生":
        person_digital["16"] = 0.5
    elif person[label["16"]] == "大学本科":
        person_digital["16"] = 0.1
    elif person[label["16"]] == "博士研究生":
        person_digital["16"] = 1
    else:
        person_digital["16"] = 0

    # 年级排名
    # print type(grade_dig(person[label["17"]]))
    # print count
    person_digital["22"] = grade_dig(person[label["22"]])

    # 将person_digital转换为json
    j_person_digital = json.dumps(person_digital, encoding='utf-8', ensure_ascii=False, sort_keys=True)

    # 储存评分内容
    output_people.write(j_person_digital+'\n')

# 关闭打开的文件
input_people.close()
output_people.close()
label_file.close()
