import pymysql

host = 'host'
port = 3306
user = 'user'
password = 'password'
dtb = 'database'

class Auth_Mysql:
    def __init__(self, host, port, user, password, dtb):
        self.connection = pymysql.connect(
            host = 'host',
            port = 3306,
            user = 'user',
            password = 'password',
            database='database',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select_gazprom(self):
        try:
            query = "SELECT ip, namber, address, tip, region, comment FROM gazprom "
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            return result
        except ValueError:
            print('Error message: ')

    # список БС
    def select_list_bs(self):
        try:
            query = 'SELECT * FROM baz'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # индивидуальные трассы к БС
    def select_ind_bs(self):
        try:
            query = 'SELECT * FROM bs'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # индивидуальный wifi, общественный wifi
    def wifi_free(self):
        try:
            query = 'SELECT * FROM wifi_public'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    def wifi_most(self):
        try:
            query = 'SELECT * FROM wifi'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # мануал по оборудованию
    def select_manual(self):
        try:
            query = 'SELECT tip, comment FROM pol'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # список АСКУЭ
    def select_ascue(self):
        try:
            query = 'SELECT id, sity, street, namber, askue FROM baza'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # список ключей
    def select_keys(self):
        try:
            query = 'SELECT * FROM ks'
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # разделение по кластерам
    def select_claster(self, claster):
        try:
            query = 'SELECT id, sity, street, namber, comment FROM baza WHERE claster = %s'
            with self.connection.cursor() as cursor:
                cursor.execute(query, claster)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    # разделение по улицам
    def select_street(self, street):
        try:
            query = 'SELECT id, sity, street, namber, comment FROM baza WHERE street = %s'
            with self.connection.cursor() as cursor:
                cursor.execute(query, street)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    def searth_bs_namber(self, searth_namber):
        try:
            query_support = "SELECT  b_namber, b_address, b_comment  FROM baz WHERE b_namber = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(query_support, (searth_namber,))
                result = cursor.fetchone()
                res = {v:k for k, v in result.items()}
                result = ', '.join(str(value) for value in res if value is not None)
                return result
        except ValueError:
            print('Error message: ' )

    def search_bs_address(self, searth_bs_address):
        try:
            query_support = "SELECT b_namber, b_address, b_comment FROM baz WHERE b_address LIKE '%" + searth_bs_address + "%'"
            with self.connection.cursor() as cursor:
                cursor.execute(query_support)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    def update_ifo(self, ssid, comment):
        query_update = "UPDATE baza SET comment = %s WHERE id = " + ssid
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_update, (comment,))
                self.connection.commit()
        except:
            self.connection.rollback()
        print(cursor.rowcount, "\n1  Добавлено  |  -1 Не добавлено")
        print(query_update)

    def insert_reestr(self, reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector):
        sql = "insert into info(reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector) values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector))
                self.connection.commit()
        except:
            self.connection.rollback()
        print(cursor.rowcount, "\n1  Добавлено  |  -1 Не добавлено")

    def support_export_csv(self):
        query_support = "SELECT * FROM `replacement` ORDER BY id"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_support)
                result = cursor.fetchall()
            return result
        except:
            self.connection.rollback()

    def sel_import(self):
        try:
            query_1 = 'SELECT id, reestr, date, sity, street, home, apartment, name FROM info ORDER BY id DESC LIMIT 20'
            with self.connection.cursor() as cursor:
                cursor.execute(query_1)
                result = cursor.fetchall()
                return result
        except ValueError:
            print('Error message: ')

    def view_replacement(self):
        query_7 = 'SELECT * FROM replacement ORDER BY id DESC LIMIT 10'
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_7)
                result = cursor.fetchall()
                return result
        except OSError as err:
            print('Error message: ')

    def select_all_people(self, date_3, date_4):
        query_3 = "SELECT street FROM info WHERE date BETWEEN %s AND %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_3, (date_3, date_4))
                result = cursor.fetchall()
                return result
        except OSError as err:
            print('Error message: ')

    def query_sum(self, date_3, date_4):
        query_sum_cable = "SELECT SUM(cable_1 + cable_2 + cable_3) AS total_sum FROM `info` WHERE date BETWEEN %s AND %s"
       # query_sum_cable = ("SELECT SUM(cable_1), SUM(cable_2), SUM(cable_3) FROM info WHERE date BETWEEN %s AND %s")
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_sum_cable, (date_3, date_4))
                res = cursor.fetchone()
                result = {v:k for k, v in res.items()}
                print(result)
                for row in result:
                    return row

        except OSError as err:
            print('Error message: ')

    def csv_export_replacement(self):
        query_support = "SELECT * FROM `replacement` ORDER BY id"
        with self.connection.cursor() as cursor:
            cursor.execute(query_support)
            result = cursor.fetchall()
            print('результат \n', result)
            return result

    def csv_export_fttx(self, date_1, date_2):
        query_2 = "SELECT * FROM info WHERE date BETWEEN %s AND %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_2, (date_1, date_2))
            result = cursor.fetchall()
            print('результат \n', result)
            return result

    def insert_replacement(self, date, address, equipment, problem, responsible):
        sql = "INSERT INTO `replacement` (date, address, equipment, problem, responsible) values( %s, %s, %s, %s, %s )"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, (date, address, equipment, problem, responsible))
                cursor.connection.commit()
                print("\n1  Добавлено  |  -1 Не добавлено")
                return
            except ValueError:
                print('Error message: ')

    def update_info(self, ssid, comment):
        query_update = "UPDATE baza SET comment = %s WHERE id = %s"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query_update, (ssid, comment))
                cursor.connection.commit()
            except ValueError:
                cursor.connection.rollback()
            print(cursor.rowcount, "\n1  Добавлено  |  -1 Не добавлено")

