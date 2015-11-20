# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import codecs

# 建立评分细则

# 第一阶段可直接数字化的项有 7是否接受调剂 8婚姻状况 9海外经历
# 10政治面貌 11亲友关系 12实习与否 13是否报考硕博 15学校级别(读json) 17学历 18学位
# 23年级排名 51奖学金级别 57英语等级和分数 期望月薪（留议)


# 打开输入文件
input_people = codecs.open("./data_under_doing/employer", 'r', encoding='utf-8')
output_people = codecs.open("./data_under_doing/employer_digital", 'w', encoding='utf-8')
label_file = codecs.open("./data_under_doing/label_employed.json", 'r', encoding='utf-8')
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
    if person[label["7"]] == "是":
        person_digital["7"] = 1
    else:
        person_digital["7"] = 0

    # 婚姻状况
    if person[label["8"]] == "已婚":
        person_digital["8"] = 1
    else:
        person_digital["8"] = 0

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

    # 实习与否
    if person[label["12"]] == "是":
        person_digital["12"] = 1
    else:
        person_digital["12"] = 0

    # 是否报考硕博
    if person[label["13"]] == "是":
        person_digital["13"] = 1
    else:
        person_digital["13"] = 0

    # 学校级别
    school_name = person[label["15"]]
    person_digital["15"] = school_digitalize(school_name, school_info)

    # 学历
    if person[label["17"]] == "硕士研究生":
        person_digital["17"] = 0.5
    elif person[label["17"]] == "大学本科":
        person_digital["17"] = 0.1
    elif person[label["17"]] == "博士研究生":
        person_digital["17"] = 1
    else:
        person_digital["17"] = 0

    # 年级排名
    # print type(grade_dig(person[label["17"]]))
    # print count
    person_digital["23"] = grade_dig(person[label["23"]])

    # 奖学金级别
    if person[label["51"]] == "国家级":
        person_digital["51"] = 1
    elif person[label["51"]] == "院校级":
        person_digital["51"] = 0.5
    else:
        person_digital["51"] = 0

    # 英语等级和分数
    try:
        if person[label["57"]] == "CET6":
            person_digital["57"] = (int(person[label["58"]])-400)/100
        elif person[label["57"]] == "CET4":
            person_digital["57"] = (int(person[label["58"]])-400)/200
        elif person[label["57"]] == "TOEFL":
            person_digital["57"] = (int(person[label["58"]])-400)/25
        else:
            person_digital["57"] = 0
    except:
        person_digital["57"] = -1

    # 将person_digital转换为json
    j_person_digital = json.dumps(person_digital, encoding='utf-8', ensure_ascii=False, sort_keys=True)

    # 储存评分内容
    output_people.write(j_person_digital+'\n')

# 关闭打开的文件
input_people.close()
output_people.close()
label_file.close()
