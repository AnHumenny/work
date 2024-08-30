import pymysql
import pymysql.cursors
from mysql.connector import connect
import csv
from markupsafe import Markup
import os

conn = connect(user='user', password='password', host='hosr', database='db_name')
class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

host = 'host'
port = 3306
user = 'user'
password = 'password'
dtb = 'db_name'

class AuthMysql:
    def __init__(self, host, port, user, password, dtb):
        self.connection = pymysql.connect(
            host = 'host',
            port = 3306,
            user = 'port',
            password = 'password',
            database='db_name',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select_gazprom(self):
        with self.connection.cursor() as cursor:
            select_all = "select * from gazprom"
            cursor.execute(select_all)
            res = cursor.fetchall()
            return res

    def select_bs(self):
        with self.connection.cursor() as cursor:
            select_all = "select * from baz"
            cursor.execute(select_all)
            res = cursor.fetchall()
            return res

    def select_manual(self):
        with self.connection.cursor() as cursor:
            select_all = "select * from pol"
            cursor.execute(select_all)
            res = cursor.fetchall()
            return res

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

    def search_info(self, street, home):
        query = "SELECT * FROM `info` WHERE street = %s AND home = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (street, home))
            result = cursor.fetchone()
        return result

    def select_info_detail_fttx(self, value):
        spl = value.split(', ')
        city = spl[1].strip()
        street = spl[2].strip()
        namber = spl[3].strip()
        try:
            with self.connection.cursor() as cursor:
                query = "select sity, claster, street, namber, comment, askue from baza WHERE sity=%s AND street=%s AND namber=%s "
                cursor.execute(query, (city, street, namber))
                res = cursor.fetchone()
                if res is not None:
                    return res
                else:
                    return ({'Улица': 'нет данных', 'инфо': 'отсутствует информация'})
        except ValueError:
            print('Что то не то с данными :(')

    def select_info_detail_fttx_only_street(self, value):
        spl = value.split(', ')
        city = spl[1].strip()
        street = spl[2].strip()
        try:
            with self.connection.cursor() as cursor:
                query = "select * from baza WHERE sity=%s AND street=%s"
                cursor.execute(query, (city, street))
                res = cursor.fetchall()
                if res is not None:
                    return res
                else:
                    return({'Улица': 'нет данных', 'инфо': 'отсутствует информация'})
        except ValueError:
            print('Что то не то с данными :(')
    def select_namber_bs(self, value):
        spl = value.split(', ')
        namber = spl[1].strip()
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT b_address, b_comment, b_namber FROM baz WHERE b_namber=%s "
                cursor.execute(query, (namber, ))
                res = cursor.fetchone()
                if res is not None:
                    return res
                else:
                    return({'БС': 'нет данных', 'инфо': 'отсутствует информация'})
        except ValueError:
            print('Что то не то с данными :(')

    def select_claster_fttx(self, value):
        spl = value.split(', ')
        city = spl[1].strip()
        claster = spl[2].strip()
        try:
            with self.connection.cursor() as cursor:
                query = "select * from baza WHERE sity=%s AND claster=%s "
                cursor.execute(query, (city, claster ))
                res = cursor.fetchall()
                if res is not None:
                    return res
                else:
                    return({'По кластерам': 'нет данных', 'инфо': 'отсутствует информация'})
        except ValueError:
            print('Что то не то с данными :(')

    def select_azs(self, value):
        spl = value.split(', ')
        azs = spl[1].strip()
        try:
            with self.connection.cursor() as cursor:
                query = "select ip, namber, address, tip, region, comment from gazprom WHERE namber=%s"
                cursor.execute(query, (azs, ))
                res = cursor.fetchone()
                if res is not None:
                    return res
                else:
                    return ('По запросу {azs} не данных')
        except ValueError:
            print('Что то не то с данными :(')

    def select_keys(self, value):
        spl = value.split(', ')
        street = spl[2].strip()
        namber = spl[3].strip()
        query = "SELECT k_entrance, k_ind, k_stand FROM ks WHERE k_street=%s AND k_home=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (street, namber))
                res = cursor.fetchone()
                if res is not None:
                    entrance = res.get('k_entrance')
                    ind = res.get('k_ind')
                    stand = res.get('k_stand')
                    result = (f'Количество подьездов: {entrance}, индивидуальных ключей: {ind}, '
                              f'стандартных ключей {stand}')
                else:
                    result = 'Нет детальных данных'

        except ValueError:
            print('Что то не то с данными :(')
        return result

    def select_year(self, date_1, date_2):
        date = date_1[:4]
        query = "SELECT cable_1, cable_2, cable_3 FROM `info` WHERE date BETWEEN %s AND %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (date_1, date_2))
            result = cursor.fetchall()
            count, cable = 0, 0
            for rows in result:
                count += 1
                res_eq = {v: k for k, v in rows.items()}
                for row in res_eq:
                    cable += int(row)
            result = (f'В {date} году подключилось {count} абонентов <br>'
                      f'Затрачено {cable} метра кабеля <br>'
                      f'Среднее количество абонентов в месяц {round(count/12)} человек<br>'
                      f'Средний расход кабеля на абонента {round(cable/count)} метров<br><br>')
            return result

    def create_new_user(self, login, status, password):
        query = 'INSERT INTO `users`(login, status, password) VALUES(%s, %s, %s)'
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (login, status, password))
                cursor.connection.commit()
                return True
        except:
            return False

    def select_user(self, login, password):
        query = "SELECT * FROM `users` WHERE login = %s AND password = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (login, password))
            result = cursor.fetchone()
            print('результат в фунтке', result)
            return result

    def select_old_user(self):
        query = 'SELECT * FROM info ORDER BY id DESC LIMIT 20'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def insert_new_fttx(self, reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector):
        query = 'INSERT INTO `info`(reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector))
                cursor.connection.commit()
                return
            except ValueError:
                print('некорректные данные ')
    def select_old_replacement(self):
        query = 'SELECT * FROM replacement ORDER BY id DESC LIMIT 20'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def insert_new_replacement(self, tip, data, address, problem, equip):
        query = 'INSERT INTO `replacement`(date, address, equipment, problem, responsible) VALUES( %s, %s, %s, %s, %s )'
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (data, address, tip, problem, equip))
                cursor.connection.commit()
                return
            except ValueError:
                print('некорректные данные ')

    def select_ssid_user(self, ssid):
        query = 'SELECT * FROM `info` WHERE id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (ssid, ))
            result = cursor.fetchone()
            if result is None:
                return False
            else:
                return result

    def update_info(self, ssid, reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector):
        query = "UPDATE info SET reestr=%s, date=%s, sity=%s, street=%s, home=%s, apartment=%s, name=%s, cable_1=%s, cable_2=%s, cable_3=%s, connector=%s WHERE id=%s"
        print('ssid in app', ssid)
        with self.connection.cursor() as cursor:
            cursor.execute(query, (reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector, ssid))
            cursor.connection.commit()
            return

    def select_ssid_replacement(self, ssid):
        query = 'SELECT * FROM `replacement` WHERE id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (ssid, ))
            result = cursor.fetchone()
            if result is None:
                return False
            else:
                return result

    def update_replacement(self, ssid, all):
        query = "UPDATE replacement SET date=%s, address=%s, equipment=%s, problem=%s, responsible=%s WHERE id=%s"
        print('ssid in app', ssid)
        with self.connection.cursor() as cursor:
            cursor.execute(query, (*all, ssid))
            cursor.connection.commit()
            return

    def select_auth_user(self):
        query = "SELECT id, login, status FROM `users` ORDER BY status"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def select_reg_user(self, name):
        query = "SELECT login FROM `users` WHERE login = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (name, ))
            result = cursor.fetchall()
            if result is None:
                return False
            else:
                return True
