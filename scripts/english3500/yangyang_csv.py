import csv
import sys
import codecs


word_col = ["17_1", "17_2", "17_3", "18_1", "18_2", "18_3", "19_1", "19_2",
            "19_3"]

def parse_old():

    words = {}
    headers = []


    file = codecs.open('word_list/yangyang3500_14_15.csv', encoding="utf-8")
    
    csvFile = csv.reader(file)
    
    line_cnt = 0
    for line in csvFile:
        if (line_cnt == 0):
            headers = line
            line_cnt += 1
            continue

        for word_ndx in range(1, len(line), 2):
            header = headers[word_ndx]
            word = line[word_ndx].strip()
            print('here %d %s'%(line_cnt, word))
            if word == "":
                # skip empty ones
                continue
            if "/" in word:
                word = word.split("/")[0]

            if (header not in words):
                words[header] = [word]
            else:
                words[header].append(word)

        line_cnt += 1
    return words

    # print (words)
    # print (words.keys())


def parse(page_num):
    # reload(sys)
    # sys.setdefaultencoding("utf-8")
    # print("calling parser")

    words = [[],[]]
    headers = []
    # yangyang3500_04_05
    if page_num < 10:
        str_num = '0' + str(page_num)
    else:
        str_num = str(page_num)
    file = codecs.open('word_list/yangyang3500_%s.csv'%str_num, encoding="utf-8")
    csv_file = csv.reader(file)
    line_cnt = 0
    for line in csv_file:
        if line_cnt == 0:
            # headers = line
            line_cnt += 1
            continue

        for word_ndx in [1, 4]:
            word = line[word_ndx].strip()
            if "/" in word:
                word = word.split("/")[0]

            if word == "":
                # skip empty ones
                continue
            if word_ndx == 1:
                words[0].append(word)
            else:
                words[1].append(word)
        
        # print line_cnt
        line_cnt += 1

    # print(words)
    # print(words.keys())

    return {'page_%s'%str_num: words[0] + words[1]}


print(parse(6))
# print(parse_old())
