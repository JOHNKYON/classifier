# -*- coding: utf-8 -*-

import json
import codecs

'''input_file = codecs.open("./label_employed", 'r', encoding='utf-8')
output_file = codecs.open("./label_employed.json", 'w', encoding='utf-8')

file = input_file.read()

file_list = file.split('\t')

dic = dict()

for index in range(1, 104):
    dic[index] = file_list[index-1]

jdic = json.dumps(dic, ensure_ascii=False, encoding='utf-8')

output_file.write(jdic)

input_file.close()
output_file.close()'''

input_file_1 = codecs.open("./label_employed.json", 'r', encoding='utf-8')
input_file_2 = codecs.open("./employed.txt", 'r', encoding='utf-8')
output_file = codecs.open("./employer2", 'w', encoding='utf-8')

# 解码label
jlabel = input_file_1.read()
label = json.loads(jlabel)
people = list()

for line in input_file_2.readlines():
    person = dict()
    person_origin = line.split('\t')
    for index in range(1, 104):
        try:
            person[label[str(index)]] = person_origin[index-1]
        except:
            person[label[str(index)]] = "-1"

    j_person = json.dumps(person, ensure_ascii=False, encoding='utf-8')
    people.append(j_person)

for l in people:
    output_file.write(l+'\n')

input_file_1.close()
input_file_2.close()
output_file.close()
