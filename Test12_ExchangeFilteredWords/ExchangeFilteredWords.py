#! /usr/bin/env python

# -*- coding: utf8 -*-

__author__ = "call_fold"

import Test11_FilteredWords.FilteredWords


def exchange_filtered_words(input_str, filtered_words_set):
    out_str = input_str
    for word in filtered_words_set:
        word_len = len(word)
        exchange_part = '*' * word_len
        out_str = out_str.replace(word, exchange_part)
    print(out_str)

if __name__ == '__main__':
    words_set = Test11_FilteredWords.FilteredWords.get_filter_words('filtered_words.txt')
    flag = True
    while flag:
        my_input_str = input('Input a word: ')
        if '#' == my_input_str:
            flag = False
        exchange_filtered_words(my_input_str, words_set)