#! /usr/bin/env python

# -*- coding: utf8 -*-

__author__ = "call_fold"


def get_filter_words(file_path):
    filtered_words_set = set()
    file = open(file_path, 'r')
    for line in file:
        for word in line.split():
            filtered_words_set.add(word)
    return filtered_words_set

def judge_input_word(input_str, filtered_words_set):
    if input_str in filtered_words_set:
        print('Freedom')
    else:
        print('Human Rights')

if __name__ == '__main__':
    words_set = get_filter_words('filtered_words.txt')
    flag = True
    while flag:
        input_word = input('Input a word: ')
        if '#' == input_word:
            flag = False
        judge_input_word(input_word, words_set)
