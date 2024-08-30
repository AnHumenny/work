import pymysql
import csv

host = 'host'
port = 3306
user = 'user'
password = 'password'
dtb = 'db_1'
dtbs = 'db_2'

class Auth_Mysql:
    def __init__(self, host, port, user, password, dtbs):
        self.connection = pymysql.connect(
            host='host',
            port=3306,
            user='user',
            password='password',
            database='db_1',
            cursorclass=pymysql.cursors.DictCursor
        )

    def check_admin(self, login, password):
        query_authent = "SELECT id, login, password, access FROM `users` WHERE login = %s AND password = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_authent, (login, password))
            result = cursor.fetchone()
            if result is not None:
                return True
            else:
                return False

    def check_superadmin(self, login, password):
        query_authent = "SELECT id, login, password, access FROM `users` WHERE login = %s AND password = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_authent, (login, password))
            result = cursor.fetchone()
            answer = result.get('access')
            if answer == 'superadmin':
                return True
            else:
                return False

    def select_all_users(self):
        query_all = "SELECT name, login, access FROM `users` ORDER BY id"
        with self.connection.cursor() as cursor:
            cursor.execute(query_all)
            result = cursor.fetchall()
            return result

    def insert_new_user(self, name, login, password, status):
        query_new_user = "INSERT INTO `users` (name, login, password, access) VALUES ( %s, %s, %s, %s )"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_new_user, (name, login, password, status))
                cursor.connection.commit()

            return True
        except pymysql.err.OperationalError:
            print('Некорректные данные')

    def delete_user(self, login):
        query_dlt_user = "DELETE FROM `users` WHERE login = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_dlt_user, (login, ))
            cursor.connection.commit()
            return
    def check_login(self, login):      #проверка существующего пользователя
        query_check_login = "SELECT login FROM `users` WHERE login = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_check_login, (login, ))
            result = cursor.fetchall()
            print(result)
            if len(result) > 0:
                return False
            else:
                return True

class Sql_Equipment:                 #переписать под наследование !!!
    def __init__(self, host, port, user, password, dtb):
        self.connection = pymysql.connect(
            host='host',
            port=3306,
            user='user',
            password='password',
            database='db_2',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select_equipment_result(self, equip):
        query_equip = "SELECT * FROM `replacement` WHERE equipment LIKE '%" + equip + "%'"
        with self.connection.cursor() as cursor:
            cursor.execute(query_equip)
            result_equip = cursor.fetchall()
            return result_equip

    def select_equipment_name(self, name):
        query_name_equip = "SELECT * FROM `replacement` WHERE responsible LIKE '%" + name + "%'"
        with self.connection.cursor() as cursor:
            cursor.execute(query_name_equip)
            result_query = cursor.fetchall()
            return result_query

    def select_adresses_equipment(self, address):
        query_address = "SELECT * FROM `replacement` WHERE address LIKE '%" + address + "%'"
        with self.connection.cursor() as cursor:
            cursor.execute(query_address)
            res_address = cursor.fetchall()
            return res_address

    def select_ascue_all(self):
        query_ascue = "SELECT id, sity, street, namber, askue FROM `baza` "
        with self.connection.cursor() as cursor:
            cursor.execute(query_ascue)
            res_ascue = cursor.fetchall()
            return res_ascue

    def insert_equip(self, equipment, address, date, problem, responsible):
        query_insert = "INSERT INTO `replacement` (equipment, address, date, problem, responsible) VALUES (%s, %s, %s, %s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(query_insert, (equipment, address, date, problem, responsible))
            self.connection.commit()
            return

    def res_add(self):
        query_insert_add = "SELECT equipment, address, date, problem, responsible FROM `replacement` WHERE id=LAST_INSERT_ID()"
        with self.connection.cursor() as cursor:
            cursor.execute(query_insert_add)
            result = cursor.fetchone()
            return result

    def csv_export(self):
        query_support = "SELECT * FROM `replacement` ORDER BY id"
        with self.connection.cursor() as cursor:
            cursor.execute(query_support)
            result = cursor.fetchall()
            print('результат \n', result)
            return result

    def searth_ascue_street(self, street):
        query_ascue = "SELECT id, sity, street, namber, askue FROM `baza` WHERE street LIKE '%" + street + "%'"
        with self.connection.cursor() as cursor:
            cursor.execute(query_ascue)
            searth_street = cursor.fetchall()
            return searth_street

    def street_with_namber(self, street, home):
        query_ascue_address = "SELECT * FROM `baza` WHERE street = %s AND namber = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_ascue_address, (street, home))
            searth_street = cursor.fetchone()
            return searth_street

    def search_ascue_ip(self, ip):
        query_ip = "SELECT * FROM `baza` WHERE askue = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_ip, (ip, ))
            search_ip = cursor.fetchone()
            print(search_ip)
            return search_ip

    def select_ascue_del(self):
        del_ascue = "SELECT id, sity, street, namber, askue FROM `baza` WHERE askue LIKE '%снят%' OR askue LIKE '%демонтирован%'"
        with self.connection.cursor() as cursor:
            cursor.execute(del_ascue)
            res_del = cursor.fetchall()
            return res_del

    def __del__(self):
        self.connection.close()
