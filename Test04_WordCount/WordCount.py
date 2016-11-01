__author__ = "call_fold"

import re
import Test03_SaveRandomNumToRedis.SaveRandomNumToRedis

def word_count(path):
    file = open(path, 'r')

    _wordcount = {}

    for line in file:
        new_line = re.sub('[^a-zA-Z]', ' ', line)
        for word in new_line.split():
            if word not in _wordcount:
                _wordcount[word] = 1
            else:
                _wordcount[word] += 1

    file.close()

    # sorted_wordcount = sorted(_wordcount.items(), key=operator.itemgetter(1), reverse=True)
    sorted_wordcount = sorted(_wordcount.items(), key=lambda x: x[1], reverse=True)

    return sorted_wordcount

def top_n(input_wordcount, n):

    top_n_list = []

    for i in range(n):
        top_n_list.append(input_wordcount[i])

    return top_n_list

if __name__ == '__main__':
    wordcount = word_count('LICENSE.md')
    num_topN = 10
    topN = top_n(wordcount, num_topN)
    table_name = 'word_count_top_n'
    Test03_SaveRandomNumToRedis.SaveRandomNumToRedis.save_to_redis(table_name, topN)
    Test03_SaveRandomNumToRedis.SaveRandomNumToRedis.print_list_from_redis(table_name)
