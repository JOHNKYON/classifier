# -*- coding: utf-8 -*-

import json
import codecs

import re
'''input_file = codecs.open("./data_under_doing/label_employed", 'r', encoding='utf-8')
output_file = codecs.open("./data_under_doing/label_employed.json", 'w', encoding='utf-8')

file = input_file.read()

file_list = file.split('\t')

dic = dict()

for index in range(1, 104):
    dic[index] = file_list[index-1]

jdic = json.dumps(dic, ensure_ascii=False, encoding='utf-8')

output_file.write(jdic)

input_file.close()
output_file.close()'''

input_file_1 = codecs.open("./data_under_doing/label_unemployed.json", 'r', encoding='utf-8')
input_file_2 = codecs.open("./data_under_doing/unemployed.txt", 'r', encoding='utf-8')
output_file = codecs.open("./data_under_doing/loser", 'w', encoding='utf-8')

# 解码label
jlabel = input_file_1.read()
label = json.loads(jlabel)
people = dict()
#count = 0

for line in input_file_2.readlines():
    # 加装每个人的数据为json
    person = dict()
    person_origin = line.split('\t')

    for index in range(2, 104):
        try:
            person[label[str(index)]] = person_origin[index-1]
        except:
            person[label[str(index)]] = "-1"

    j_person = json.dumps(person, ensure_ascii=False, encoding='utf-8', sort_keys=True)
    # 每个人的Key为他的申请表编号
    '''if not(re.match('\d+', person_origin[0])):
        print count
    count += 1'''

    '''if count == 4251:
        print person_origin[0]
    count += 1'''

    output_file.writelines(j_person+'\n')
    # people[person_origin[0]] = j_person

# j_people = json.dumps(people, ensure_ascii=False, indent=1, encoding='utf-8', sort_keys=True)
# output_file.write(j_people)

input_file_1.close()
input_file_2.close()
output_file.close()
