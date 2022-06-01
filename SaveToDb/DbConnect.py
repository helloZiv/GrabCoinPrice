import pymysql


def get_connect():
    db = pymysql.connect(host='localhost',
                         user='root',
                         port=3306,
                         database='blockchain')

    return db
