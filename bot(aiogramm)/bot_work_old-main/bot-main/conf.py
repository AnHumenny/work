import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


host='host',
port=5432,
user='user',
password='password',
database='db_name'


'''
def insert_entrance(user, content, time_str):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(dbname="", user="", password="",
                                      host="", port="")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        query_entrance = """INSERT INTO bot_bot (title, content, date_created) VALUES (%s, %s, %s)"""
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        cursor.execute(query_entrance, (user, content, time_str))
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
'''
class Postgre_bot:
    def __init__(self, host, port, user, password, database):
        self.connection = psycopg2.connect(
            host='host',
            port=5432,
            user='user',
            password='password',
            database='db_name'
            )

    def insert_entr(self, user, content, time_str):
        query_entrance = """INSERT INTO bot_bot (title, content, date_created) VALUES (%s, %s, %s)"""
        with self.connection.cursor() as cursor:
            cursor.execute(query_entrance, (user, content, time_str))
            cursor.connection.commit()
            return

    def __del__(self):
        self.connection.close()
