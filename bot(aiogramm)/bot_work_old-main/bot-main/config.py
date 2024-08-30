import pymysql
import base64
API_TOKEN = 'Токен'

host = 'host'
port = 3306
user = 'port'
password = 'user'
dtb = 'password'
class telega_SQL:
    def __init__(self, host, port, user, password, dtb):
        self.connection = pymysql.connect(
            host='host',
            port=3306,
            user='user',
            password='password',
            database='db_name',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select_pass(self, login, password):
        query_select_info = "SELECT login, name, password FROM pass WHERE login = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select_info, (login, ))
            result = cursor.fetchall()
            for row in result:
                return result

    def fix_time(self, name, time_string):
        query_select_info = "INSERT INTO `log_file` (user, time_string) VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select_info, (name, time_string))
            cursor.connection.commit()
            return

    def select_user(self, name):
        query_select = "SELECT name, phone, email, status, area FROM telega WHERE name LIKE'%" + name + "%'"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select)
            result = cursor.fetchall()
            if result is None:
                return False
            else:
                return result
                
    def select_admin(self, login):
        query_select = "SELECT status from telega WHERE login = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select, (login, ))
            result = cursor.fetchall()
        return result
        
    def select_info(self, street, home):
        query_select_info = "SELECT comment FROM baza WHERE street = %s AND namber = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select_info, (street, home))
            result = cursor.fetchone()
        return result
        
    def select_info_keys(self, street, home):       
        query_select_keys = "SELECT k_entrance, k_ind, k_stand FROM ks WHERE k_street = %s AND k_home = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select_keys, (street, home))
            result_keys = cursor.fetchone()  
            return result_keys     

    def group_mont(self):
        query_select = "SELECT name FROM telega"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select)
            result = cursor.fetchall()
        return result

    def group_fiks(self):
        query_select = "SELECT name, phone FROM telega"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select)
            result = cursor.fetchall()
        return result

    def add_envi(self, equipment, address, date, problem, responsible):
        equip_insert = "INSERT INTO `replacement` (equipment, address, date, problem, responsible) VALUES (%s, %s, %s, %s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(equip_insert, (equipment, address, date, problem, responsible))
            cursor.connection.commit()
            return

    def add_new_info(self, reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector):
        info_insert = "INSERT INTO `info` (reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(info_insert, (reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector))
            cursor.connection.commit()
            return

    def view_last_new_user(self):
        select_last_user = "SELECT * FROM `info` WHERE id=LAST_INSERT_ID()"
        with self.connection.cursor() as cursor:
            cursor.execute(select_last_user)
            result = cursor.fetchone()
            return result

    def sel_envi(self):
        query_select = "SELECT equipment, address, date, problem, responsible FROM `replacement` WHERE id=LAST_INSERT_ID()"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select)
            result = cursor.fetchone()
        return result

    def sel_last_envi(self, limit):
        query_select_last = "SELECT * FROM `replacement` ORDER BY id DESC LIMIT " + limit
        with self.connection.cursor() as cursor:
            cursor.execute(query_select_last)
            result = cursor.fetchall()
        return result
        
    def delete_equip(self, ssid):
        query_dlt_equip = "DELETE FROM `replacement` WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_dlt_equip, (ssid, ))
            cursor.connection.commit()
        return

    def select_address_user(self, street, home, namber):
        with self.connection.cursor() as cursor:
            query_sel_user = "SELECT * FROM info WHERE street = %s AND home = %s AND apartment = %s"
            cursor.execute(query_sel_user, (street, home, namber))
            result = cursor.fetchall()
            return result

    def select_name_user(self, name):
        with self.connection.cursor() as cursor:
            query_sel_user = "SELECT * FROM info WHERE name LIKE '%" + name + "%'"
            cursor.execute(query_sel_user)
            result = cursor.fetchall()
            return result

    def select_bs(self, namber):
        query_select = "SELECT b_namber, b_address from baz WHERE b_namber = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select, (namber, ))
            result = cursor.fetchone()
            return result

    def select_address_bs(self, address):
        query_select_bs = "SELECT b_namber, b_address from baz WHERE b_address LIKE '%" + address + "%'"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select_bs)
            result = cursor.fetchall()
        return result

    def add_new_user(self, login, name, status, password, phone, email):
        sql = "insert into `pass` (login, name, status, password, phone, email) values ( %s, %s, %s, %s, %s, %s )"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (login, name, status, password, phone, email))
                self.connection.commit()
            return
        except ValueError:
            print('упс :(')
            return
            
    def check_new_user(self, login, name, status, password, phone, email):
        query = "SELECT * FROM `pass` WHERE login = %s"
        print(login, name, status, password, phone, email)
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (login, ))
                result = cursor.fetchall()
                print(len(result))
                if len(result) == 0:
                    pass_wrd = password.encode('utf-8')
                    password = base64.b64encode(pass_wrd)
                    self.add_new_user(login, name, status, password, phone, email)
                else:
                    print('выберите другой логин :(')
            except ValueError:
                print('упс :(')

    def select_ascue_del(self):
        del_ascue = "SELECT sity, street, namber, askue FROM `baza` WHERE askue LIKE '%снят%' OR askue LIKE '%демонтирован%'"
        with self.connection.cursor() as cursor:
            cursor.execute(del_ascue)
            res_del = cursor.fetchall()
            return res_del

    def select_azs(self, namber):
        query_select = "SELECT * FROM `gazprom` WHERE namber = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query_select, (namber, ))
            result = cursor.fetchone()
            return result

    def __del__(self):
        self.connection.close()
