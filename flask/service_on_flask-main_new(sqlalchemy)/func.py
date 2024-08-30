import pymysql
import pymysql.cursors
from mysql.connector import connect
import csv
from markupsafe import Markup
import os

conn = connect(user='user', password='password', host='localhost', database='database')
class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

host = 'host'
port = 3306
user = 'user'
password = 'password'
dtb = 'database'

class AuthMysql:
    def __init__(self, host, port, user, password, dtb):
        self.connection = pymysql.connect(
            host='host',
            port=3306,
            user='user',
            password='password',
            database='database',
            cursorclass=pymysql.cursors.DictCursor
        )

    
    def index(self):
        with open('data/year_2022.csv') as data:
            read = csv.reader(data)
            count, cable = 0, 0
            for row in read:
                count += 1
                cable += int(row[8]) + int(row[9])   #int(row[10])  некорректные данные в csv
            greeting_1 = Markup(f'В 2022м году подключилось <strong>{count}</strong> абонентов, затрачено<strong> {cable}</strong> метра кабеля')
        with open('data/year_2023.csv') as data:
            read = csv.reader(data)
            count, cable = 0, 0
            for row in read:
                count += 1
                cable += int(row[8]) + int(row[9])   #int(row[10])  некорректные данные в csv
        greeting_2 = (f'В 2023м году подключилось {count} абонентов, затрачено {cable} метра кабеля')
        query = "SELECT cable_1, cable_2, cable_3 FROM `info` WHERE date BETWEEN %s AND %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, ('2024-01-01', '2024-12-31'))
            result = cursor.fetchall()
            count, cable = 0, 0
            for rows in result:
                count += 1
                res_eq = {v: k for k, v in rows.items()}
                for row in res_eq:
                    cable += int(row)
        greeting_3 = (f'В 2024м году подключилось {count} абонентов, затрачено {cable} метра кабеля')
        greeting = [greeting_1, greeting_2, greeting_3]
        return greeting

    def select_by_year_2021(self):
        query = "SELECT COUNT(*) FROM `info` WHERE date BETWEEN '2021-01-01' AND '2021-12-31' GROUP BY DATE_FORMAT(date, '%Y-%m')"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result


    def select_by_year_2022(self):
        query = "SELECT COUNT(*) FROM `info` WHERE date BETWEEN '2022-01-01' AND '2022-12-31' GROUP BY DATE_FORMAT(date, '%Y-%m')"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def select_by_year_2023(self):
        query = "SELECT COUNT(*) FROM `info` WHERE date BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY DATE_FORMAT(date, '%Y-%m')"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
        return result

    def select_by_year_2024(self):
        query = "SELECT COUNT(*) FROM `info` WHERE date BETWEEN '2024-01-01' AND '2024-12-31' GROUP BY DATE_FORMAT(date, '%Y-%m')"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result


