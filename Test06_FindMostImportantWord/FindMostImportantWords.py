__author__ = "call_fold"

import Test04_WordCount.WordCount
import Test05_ChangePictureDPI.ChangePictureDPI
import IgnoreWordList.IgnoreWordList
import os


def find_most_important_words(source_path, kind_of_file, num_of_words):
    file_name_list = Test05_ChangePictureDPI.ChangePictureDPI.get_files_name(source_path, kind_of_file)
    most_important_word_list = []

    for file_name in file_name_list:
        file_path = source_path + '/%s' % file_name
        ignore_word_list = IgnoreWordList.IgnoreWordList.ignore_word_list
        my_word_list = Test04_WordCount.WordCount.word_count(file_path, ignore_word_list)
        topN_list = Test04_WordCount.WordCount.top_n(my_word_list, num_of_words)
        print(topN_list)
        most_important_word_list.append((file_name, topN_list[0][0]))

    return most_important_word_list


if __name__ == '__main__':
    word_list = find_most_important_words(os.path.abspath('.') + '/text', 'txt', 1)
    print(word_list)
