__author__ = "call_fold"

import redis
import Test01_CreateRandomNum.CreateRandomNum


def save_to_redis(_table_name, code_list):
    strictRedis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    strictRedis.delete(_table_name)
    for code in code_list:
        strictRedis.rpush(_table_name, code)


def print_list_from_redis(_table_name):
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    list_len = r.llen(_table_name)
    return_list = r.lrange(_table_name, 0, list_len)
    for return_code in return_list:
        print(return_code)


if __name__ == '__main__':
    codeList = Test01_CreateRandomNum.CreateRandomNum.createNum(200, 10)
    table_name = 'random_num'
    save_to_redis(table_name, codeList)
    print_list_from_redis(table_name)
