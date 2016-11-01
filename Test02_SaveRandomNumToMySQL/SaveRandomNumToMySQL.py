__author__ = "call_fold"
import pymysql.cursors
import Test01_CreateRandomNum.CreateRandomNum


def saveToMySQL(list):
    connection = pymysql.connect(host='139.129.41.15',
                                 user='root',
                                 password='slf',
                                 db='python_test',
                                 charset='utf8')

    try:
        with connection.cursor() as cursor:
            sqlDelete = "DROP TABLE IF EXISTS random_num"
            cursor.execute(sqlDelete)

        connection.commit()

        with connection.cursor() as cursor:
            sqlCreate = 'CREATE TABLE random_num (id INT(11) NOT NULL AUTO_INCREMENT, code VARCHAR(255), PRIMARY KEY (id)) CHARACTER SET utf8 AUTO_INCREMENT = 1'
            cursor.execute(sqlCreate)

        connection.commit()

        with connection.cursor() as cursor:
            sqlInsert = "INSERT INTO random_num (code) VALUES (%s)"
            cursor.executemany(sqlInsert, list)

        connection.commit()

    finally:
        connection.close()


if __name__ == '__main__':
    codeList = Test01_CreateRandomNum.CreateRandomNum.createNum(200, 10)
    print(codeList)
    saveToMySQL(codeList)
