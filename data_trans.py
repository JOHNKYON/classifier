# -*- coding: utf-8 -*-

import codecs
import json

# 打开输入，输出文件
input_file = codecs.open("./data.txt", 'r', encoding='utf-8')
fp = codecs.open("./data.json", 'w', encoding='utf-8')
# 建立json
count = 0
people = dict()
person = dict()
for line in input_file.readlines():
    if count == 0:
        count += 1
        continue
    else:
        segment = line.split('\t')
        person["age"] = segment[0]
        person["income"] = segment[1]
        person["student"] = segment[2]
        person["credit_rating"] = segment[3]
        person["buy"] = segment[4]
        # 第一层转换为json
        j_person = json.dumps(person, ensure_ascii=False)
        people[count] = j_person
        count += 1
j_people = json.dumps(people, ensure_ascii=False, indent=1)


fp.write(j_people)


# 关闭输入，输出文件
input_file.close()
fp.close()

