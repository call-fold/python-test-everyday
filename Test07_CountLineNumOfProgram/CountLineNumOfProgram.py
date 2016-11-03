__author__ = "call_fold"

import os
import Common.FileCommon


def count_line(source_path):
    file_name_list = Common.FileCommon.get_file_name_list(source_path)
    target_list = []
    for file_name in file_name_list:
        file_path = source_path + '/' + file_name
        file_len = Common.FileCommon.file_len(file_path)
        target_list.append((file_name, file_len))
    return target_list


if __name__ == '__main__':
    line_list = count_line(os.path.abspath('.') + '/program')
    print(line_list)
