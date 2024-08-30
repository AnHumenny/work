import autent
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
import base64
import csv

dtb = autent.Sql_Equipment(host=autent.host, port=autent.port, user=autent.user,
                           password=autent.password, dtb=autent.dtb)
dtbs = autent.Auth_Mysql(host=autent.host, port=autent.port, user=autent.user,
                         password=autent.password, dtbs=autent.dtbs)

class Win(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Модуль по оборудованию')
        self.geometry('900x600')
        self.shared_variable = tk.StringVar()
        self.shared_ascue = tk.StringVar()
        self.ascue_home = tk.StringVar()
        self.name = tk.StringVar()
        self.login = tk.StringVar()
        self.password = tk.StringVar()
        self.equipment = tk.StringVar()
        self.address = tk.StringVar()
        self.date = tk.StringVar()
        self.problem = tk.StringVar()
        self.responsible = tk.StringVar()
        self.status = tk.StringVar()
        self.new_name = tk.StringVar()
        self.new_login = tk.StringVar()
        self.new_password = tk.StringVar()
        self.new_status = tk.StringVar()
        self.d_user = tk.StringVar()
        self.authent_OK = False     #отключает авторизацию
        self.superadmin_OK = False   #проверка статуса админа
      #  self.resizable(False, False)   #изменение размера
        self.frame_menu = tk.Frame(self, width=200, height=600)
        self.frame_menu.pack(side=LEFT)
        self.frame_info_user = tk.Frame(self, width=700)
        self.frame_info_user.pack()
        self.frame_info = tk.Frame(self, width=700)
        self.frame_info.pack()
        self.sel_equipment = tk.Entry(self.frame_menu, width=18, textvariable=self.shared_variable)
        self.sel_equipment.grid(row=0, column=0, columnspan=2)
        self.button_sel_equipment = tk.Button(self.frame_menu, width=15,
                                              text='Тип оборудования', command=self.select_equipment)
        self.button_sel_equipment.grid(row=1, column=0, pady=5, padx=10, columnspan=2)
        self.button_name_equipment = tk.Button(self.frame_menu, width=15,
                                               text='Взято-передано', command=self.name_equipment)
        self.button_name_equipment.grid(row=2, column=0, pady=5, padx=10, columnspan=2)
        self.button_adressess_equipment = tk.Button(self.frame_menu, width=15,
                                                    text='Адрес замены', command=self.adresses_equipment)
        self.button_adressess_equipment.grid(row=3, column=0, pady=5, padx=10, columnspan=2)

        self.add_equipment = tk.Button(self.frame_menu, width=15,
                                       text='Добавить запись', command=self.add_equipment)
        self.add_equipment.grid(row=4, column=0, pady=5, padx=10, columnspan=2)
        self.button_csv_export = tk.Button(self.frame_menu, width=15,
                                           text='Экспорт в .csv', command=self.csv_export)
        self.button_csv_export.grid(row=5, column=0, pady=5, padx=10, columnspan=2)
        self.label_en = tk.Label(self.frame_menu, width=15, text='---------------')
        self.label_en.grid(row=6, column=0, pady=10, padx=5, columnspan=2)
        self.button_ascue = tk.Button(self.frame_menu, width=15, text='Данные АСКУЭ',
                                      command=self.select_ascue)
        self.button_ascue.grid(row=7, column=0, pady=5, padx=10, columnspan=2)
        self.entry_ascue = tk.Entry(self.frame_menu, width=10, textvariable=self.shared_ascue)
        self.entry_ascue.delete("0", tk.END)
        self.entry_ascue.grid(row=8, column=0, pady=5, padx=2)
        self.entry_ascue_ip = tk.Entry(self.frame_menu, width=4, textvariable=self.ascue_home)
        self.entry_ascue_ip.delete("0", tk.END)
        self.entry_ascue_ip.grid(row=8, column=1, pady=5, padx=2)
        self.searth_ascue_street = tk.Button(self.frame_menu, width=15,
                                             text='поиск по адресу', command=self.searth_street_ascue)
        self.searth_ascue_street.grid(row=10, column=0, pady=5, padx=10, columnspan=2)
        self.searth_ascue_ip = tk.Button(self.frame_menu, width=15, text='поиск по IP',
                                         command=self.search_ip)
        self.searth_ascue_ip.grid(row=11, column=0, pady=5, padx=10, columnspan=2)
        self.searth_ascue_ip = tk.Button(self.frame_menu, width=15, text='Снятые АСКУЭ',
                                         command=self.ascue_del)
        self.searth_ascue_ip.grid(row=12, column=0, pady=5, padx=10, columnspan=2)
        self.exit_user_button = tk.Button(self.frame_menu, width=15, text='Выход', command=self.exit_user)
        self.exit_user_button.grid(row=13, column=0, pady=5, padx=10, columnspan=2)

        self.label_user = tk.Label(self.frame_menu, width=15, text='---------------')
        self.label_user.grid(row=15, column=0, pady=10, padx=5, columnspan=2)
        self.button_user = tk.Button(self.frame_menu, width=15, text='Админка',
                                     command=self.select_user)
        self.button_user.grid(row=16, column=0, pady=5, padx=10, columnspan=2)

        if self.authent_OK is False:
            self.start()

    def start(self):
        for widget in self.frame_info_user.winfo_children():
            widget.destroy()
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        entry_auth = tk.Entry(self.frame_info, width=20, textvariable=self.login)
        entry_auth.delete(0, tk.END)
        entry_auth.pack(pady=10)
        entry_pass = tk.Entry(self.frame_info, width=20, show='*', textvariable=self.password)
        entry_pass.delete(0, tk.END)
        entry_pass.pack(pady=5)
        but_auth = tk.Button(self.frame_info, width=10, text='Отправить', command=self.check_user)
        but_auth.pack(pady=10)

    #блок дополнительный
    def select_user(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is True and self.superadmin_OK is True:
            add_user_button = tk.Button(self.frame_info_user, width=20,
                                        text='Добавить пользователя', command=self.add_user)
            add_user_button.grid(row=0, column=0, pady=5, padx=10)
            del_user_button = tk.Button(self.frame_info_user, width=20,
                                        text='Удалить пользователя', command=self.del_user)
            del_user_button.grid(row=0, column=1, pady=5, padx=10)

            all_user_button = tk.Button(self.frame_info_user, width=20,
                                        text='Все пользователи', command=self.all_users)
            all_user_button.grid(row=0, column=2, columnspan=2, pady=5, padx=10)
            temp_line = '-' * 50
            add_file_label = tk.Label(self.frame_info_user, width=50, text=temp_line)
            add_file_label.grid(row=1, column=0, columnspan=3, pady=5, padx=10)

            add_file_btn = tk.Button(self.frame_info_user, width=14, text='Dlink',
                                     command=self.call_dlink_files)
            add_file_btn.grid(row=2, column=0, pady=5, padx=10)

            add_file_btn = tk.Button(self.frame_info_user, width=14, text='Ubiquity',
                                     command=self.call_ubiquity_files)
            add_file_btn.grid(row=2, column=1, pady=5, padx=10)

            add_file_btn = tk.Button(self.frame_info_user, width=14, text='WAP LTE',
                                     command=self.call_wap_lte_files)
            add_file_btn.grid(row=2, column=2, pady=5, padx=10)
        else:
            superadmin_label = tk.Label(self.frame_info, width=50,
                                        text='Доступ к пользовательским данным закрыт!')
            superadmin_label.pack(pady=5)
    def add_user(self):
        if self.authent_OK is False:
            self.start()
        else:
            for widget in self.frame_info.winfo_children():
                widget.destroy()
            text_new_name_label = tk.Label(self.frame_info, width=30, text='Имя')
            text_new_name_label.pack(pady=5)
            add_new_name = tk.Entry(self.frame_info, width=15, textvariable=self.new_name)
            add_new_name.delete('0', tk.END)
            add_new_name.pack(pady=5)
            text_new_login = tk.Label(self.frame_info, width=30, text='Логин')
            text_new_login.pack(pady=5)
            add_new_login = tk.Entry(self.frame_info, width=15, textvariable=self.new_login)
            add_new_login.delete('0', tk.END)
            add_new_login.pack(pady=5)
            text_new_password = tk.Label(self.frame_info, width=30, text='Пароль')
            text_new_password.pack(pady=5)
            add_new_password = tk.Entry(self.frame_info, width=15, textvariable=self.new_password)
            add_new_password.delete('0', tk.END)
            add_new_password.pack(pady=5)
            text_new_status = tk.Label(self.frame_info, width=20, text='Статус пользователя')
            text_new_status.pack(pady=5)
            add_new_status = tk.Entry(self.frame_info, width=15, textvariable=self.new_status)
            add_new_status.delete('0', tk.END)
            add_new_status.pack(pady=5)
            add_but = tk.Button(self.frame_info, width=20,
                                text='Добавить пользователя', command=self.add_new_user)
            add_but.pack(pady=5)
            
    def add_new_user(self):
        name = self.new_name.get()
        login = self.new_login.get()
        password = self.new_password.get()
        status = self.new_status.get()
        check_new_login = dtbs.check_login(login)
        if len(password) < 8:
            text_new_status = tk.Label(self.frame_info, width=80, text='Короткий пароль')
            text_new_status.pack(pady=5)
            return
        if check_new_login is True:
            pass_word = password.encode('utf-8')
            password = base64.b64encode(pass_word)
            result = dtbs.insert_new_user(name, login, password, status)
            name_user = name
            for widget in self.frame_info_user.winfo_children():
                widget.update()
            text_new_status = tk.Label(self.frame_info, width=80,
                                       text=f'Пользователь {name_user} добавлен!')
            text_new_status.pack(pady=5)
        if check_new_login is False:
            text_new_status = tk.Label(self.frame_info, width=80, text='Такой пользователь уже есть :(')
            text_new_status.pack(pady=5)
            return
            
    def del_user(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        del_user_label = tk.Label(self.frame_info, width=30, text='Удалить пользователя по логину')
        del_user_label.pack(pady=5)
        del_user_entry = tk.Entry(self.frame_info, width=15, textvariable=self.d_user)
        del_user_entry.delete('0', tk.END)
        del_user_entry.pack(pady=5)
        del_but = tk.Button(self.frame_info, width=20,
                            text='Удалить', command=self.dlt_user)
        del_but.pack(pady=5)
        
    def dlt_user(self):
        dlt_user = self.d_user.get()
        dtbs.delete_user(dlt_user)
        self.del_user()
        
    def all_users(self):
        result = dtbs.select_all_users()
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        label_user = tk.Text(self.frame_info, width=74, height=31)
        for rows in result:
            for key, value in rows.items():
                label_user.insert(tk.END, f'{value}  ')
            label_user.insert(tk.END, '\n')
        label_user.pack(pady=5, padx=10)

    #проверка на регистрацию и админа
    def check_user(self):
        login = self.login.get()
        password = self.password.get()
        pass_word = password.encode('utf-8')
        password = base64.b64encode(pass_word)
        result = dtbs.check_admin(login, password)
        result_s_admin = dtbs.check_superadmin(login, password)
        if result is True:
            self.authent_OK = True
        if result_s_admin is True:
            self.superadmin_OK = True
        for widget in self.frame_info_user.winfo_children():
            widget.destroy()
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if result is False:
            self.authent_OK = False
            self.superadmin_OK = False
            access_close = tk.Label(self.frame_info, width=20, text='Доступ закрыт')
            access_close.pack()
            
    # отображение текстовых файлов (wap LTE)
    def call_wap_lte_files(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        try:
            name = fd.askopenfilename(
                initialdir='files/LTE',
                title="wap LTE",
                filetypes=(("txt", "*.txt"),)
            )
            with open(name, 'r', encoding='utf-8') as f:
                data = f.read()
                label_data = tk.Text(self.frame_info, width=88, height=27)
                label_data.insert(tk.END, f'{data}  ')
                label_data.pack()
            f.close()
        except Exception:
            print('не выбран файл')
            
    # отображение текстовых файлов (Dlink)
    def call_dlink_files(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        try:
            name = fd.askopenfilename(
                initialdir='files/Dlink/Gomel',
                title="Dlink",
                filetypes=(("txt", "*.txt"),)
            )
            with open(name, 'r', encoding='utf-8') as f:
                data = f.read()
                label_data = tk.Text(self.frame_info, width=88, height=27)
                label_data.insert(tk.END, f'{data}  ')
                label_data.pack()
            f.close()
        except Exception:
            print('не выбран файл')

    # отображение текстовых файлов (Ubiquity)
    def call_ubiquity_files(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        try:
            name = fd.askopenfilename(
                initialdir='files/Ubiquity/Gomel',
                title="Ubiquity",
                filetypes=(("txt", "*.txt"),)
            )
            with open(name, 'r', encoding='utf-8') as f:
                data = f.read()
                label_data = tk.Text(self.frame_info, width=88, height=27)
                label_data.insert(tk.END, f'{data}  ')
                label_data.pack()
            f.close()
        except Exception:
            print('не выбран файл')
            
    #Выборка по названию оборудования
    def select_equipment(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            equip = self.shared_variable.get()
            if equip is None:
                for widget in self.frame_info_user.winfo_children():
                    widget.destroy()
                for widget in self.frame_info.winfo_children():
                    widget.destroy()
            if dtb.select_equipment_result(equip) == '':
                for widget in self.frame_info.winfo_children():
                    widget.destroy()
            else:
                res_equip = dtb.select_equipment_result(equip)
                scrollbar = tk.Scrollbar(self.frame_info)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                my_list = tk.Text(self.frame_info, width=89, height=28,
                                  wrap=WORD, yscrollcommand=scrollbar.set)
                for rows in res_equip:
                    res_eq = {v:k for k, v in rows.items()}
                    res = ', '.join(str(value) for value in res_eq if value is not None)
                    my_list.insert(tk.END, str(res))
                    my_list.insert(tk.END, str('\n'))
                    my_list.insert(tk.END, str('-' * 30))
                    my_list.insert(tk.END, str('\n'))
                    my_list.pack()
                my_list.pack(side=tk.LEFT, fill=tk.BOTH)
                scrollbar.config(command=my_list.yview)
            del equip

    #выборка замены оборудования по имени (взял-вернул)
    def name_equipment(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            name = self.shared_variable.get()
            if name == '':
                for widget in self.frame_info_user.winfo_children():
                    widget.destroy()
                for widget in self.frame_info.winfo_children():
                    widget.destroy()
            else:
                res_name_equipment = dtb.select_equipment_name(name)
                scrollbar = tk.Scrollbar(self.frame_info)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                my_list = tk.Text(self.frame_info, width=89, height=28,
                                  wrap=WORD, yscrollcommand=scrollbar.set)
                for rows in res_name_equipment:
                    res_name_equip = {v:k for k, v in rows.items()}
                    value = ', '.join(str(value) for value in res_name_equip if value is not None)
                    my_list.insert(tk.END, str(value))
                    my_list.insert(tk.END, str('\n'))
                    my_list.insert(tk.END, str('-' * 30))
                    my_list.insert(tk.END, str('\n'))
                my_list.pack(side=tk.LEFT, fill=tk.BOTH)
                scrollbar.config(command=my_list.yview)
                del name
    #выборка замены по адресу
    def adresses_equipment(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            address = self.shared_variable.get()
            if address == '':
                for widget in self.frame_info_user.winfo_children():
                    widget.destroy()
                for widget in self.frame_info.winfo_children():
                    widget.destroy()
            else:
                result_address = dtb.select_adresses_equipment(address)
                scrollbar = tk.Scrollbar(self.frame_info)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                my_list = tk.Text(self.frame_info, width=89, height=28,
                                  wrap=WORD, yscrollcommand=scrollbar.set)
                for rows in result_address:
                    res_address = {v:k for k, v in rows.items()}
                    value = ', '.join(str(value) for value in res_address if value is not None)
                    my_list.insert(tk.END, str(value))
                    my_list.insert(tk.END, str('\n'))
                    my_list.insert(tk.END, str('-' * 30))
                    my_list.insert(tk.END, str('\n'))
                my_list.pack()
                my_list.pack(side=tk.LEFT, fill=tk.BOTH)
                scrollbar.config(command=my_list.yview)
            del address

    #добавить запись в оборудование
    def add_equipment(self):
        if self.authent_OK is False:
            self.start()
        else:
            for widget in self.frame_info.winfo_children():
                widget.destroy()
            text_new_equipment = tk.Label(self.frame_info, width=30, text='Тип оборудования')
            text_new_equipment.pack(pady=5)
            add_new_equipment = tk.Entry(self.frame_info, width=15, textvariable=self.equipment)
            add_new_equipment.delete('0', tk.END)
            add_new_equipment.pack(pady=5)
            text_new_address = tk.Label(self.frame_info, width=30, text='Адрес замены')
            text_new_address.pack(pady=5)
            add_new_address = tk.Entry(self.frame_info, width=15, textvariable=self.address)
            add_new_address.delete('0', tk.END)
            add_new_address.pack(pady=5)
            text_new_date = tk.Label(self.frame_info, width=30, text='Дата замены')
            text_new_date.pack(pady=5)
            add_new_date = tk.Entry(self.frame_info, width=15, textvariable=self.date)
            add_new_date.delete('0', tk.END)
            add_new_date.pack(pady=5)
            text_new_problem = tk.Label(self.frame_info, width=80, text='Проблема')
            text_new_problem.pack(pady=5)
            add_new_problem = tk.Entry(self.frame_info, width=50, textvariable=self.problem)
            add_new_problem.delete('0', tk.END)
            add_new_problem.pack(pady=5)
            text_new_responsible = tk.Label(self.frame_info, width=30, text='Взято-передано')
            text_new_responsible.pack(pady=5)
            add_new_responsible = tk.Entry(self.frame_info, width=30, textvariable=self.responsible)
            add_new_responsible.delete('0', tk.END)
            add_new_responsible.pack(pady=5)
            add_but = tk.Button(self.frame_info, width=20,
                                text='Добавить запись', command=self.add_equip)
            add_but.pack(pady=5)
    def add_equip(self):
        equipment = self.equipment.get()
        address = self.address.get()
        date = self.date.get()
        problem = self.problem.get()
        responsible = self.responsible.get()
        dtb.insert_equip(equipment, address, date, problem, responsible)
        result_add = dtb.res_add()
        print(result_add)
        for widget in self.frame_info_user.winfo_children():
            widget.destroy()
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        for key, value in result_add.items():
            my_list = tk.Label(self.frame_info, width=450)
            my_list['text'] = value
            my_list.pack()
        my_list_1 = tk.Label(self.frame_info, width=450, text='Добавлено!')
        my_list_1.pack()
    # экспорт в csv
    def csv_export(self):
        if self.authent_OK is False:
            self.start()
        else:
            result = dtb.csv_export()

            with open('Замена_оборудования.csv', 'w', newline="", encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL, lineterminator="\r")
                for rows in result:
                    result = {v:k for k, v in rows.items()}
                    res = ', '.join(str(value) for value in result if value is not None)
                    csv_writer.writerow([res])
                    print(res)
    def select_ascue(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            if dtb.select_ascue_all() is None:
                self.select_ascue()
            else:
                result_ascue = dtb.select_ascue_all()
                scrollbar = tk.Scrollbar(self.frame_info)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                my_list = tk.Text(self.frame_info, width=89, height=28,
                                  wrap=WORD, yscrollcommand=scrollbar.set)
                for rows in result_ascue:
                    for key, value in rows.items():
                        my_list.insert(tk.END, f'{value}  ||  ')
                    my_list.insert(tk.END, '\n')
                    my_list.pack(side=tk.LEFT, fill=tk.BOTH)
                scrollbar.config(command=my_list.yview)
    # промежуточная выборка (с номером или без номера дома)
    def searth_street_ascue(self):
        street = self.shared_ascue.get()
        home = self.ascue_home.get()
        if len(street) > 0 and len(home) == 0:
            self.searth_street_without_namber()
        elif len(street) > 0 and len(home) > 0:
            self.searth_street_with_namber()

    # поиск АСКУЭ по улице (выборка по всем улицам с похожим названием(урезанный))
    def searth_street_without_namber(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            street = self.shared_ascue.get()
            if dtb.searth_ascue_street(street) == '':
                self.start()
            else:
                result_without_number = dtb.searth_ascue_street(street)
                scrollbar = tk.Scrollbar(self.frame_info)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                my_list = tk.Text(self.frame_info, width=89, height=28,
                                  wrap=WORD, yscrollcommand=scrollbar.set)
                for rows in result_without_number:
                    for key, value in rows.items():
                        my_list.insert(tk.END, f'{value}  ||  ')
                    my_list.insert(tk.END, '\n')
                my_list.pack(side=tk.LEFT, fill=tk.BOTH)
                scrollbar.config(command=my_list.yview)
            del street

    # поиск АСКУЭ по улице и номер дома (целевое, с полной инфой)
    def searth_street_with_namber(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            home = self.ascue_home.get()
            street = self.shared_ascue.get()
            result_with_number = dtb.street_with_namber(street, home)
            my_list = tk.Text(self.frame_info, width=89, height=28, wrap=WORD)
            for key, value in result_with_number.items():
                my_list.insert(tk.END, f'{value}  ||  ')
            my_list.pack()
            del home
            del street
    # поиск АКСУЭ по ip
    def search_ip(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            ip = self.shared_ascue.get()
            result_ip = dtb.search_ascue_ip(ip)
            my_list = tk.Text(self.frame_info, width=89, height=28, wrap=WORD)
            try:
                for key, value in result_ip.items():
                    my_list.insert(tk.END, f'{value}  ||  ')
                my_list.pack()
            except AttributeError:
                print('некорректные данные ip')
            del ip
            
    # выборка снятых АСКУЭ
    def ascue_del(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        if self.authent_OK is False:
            self.start()
        else:
            result_del = dtb.select_ascue_del()
            if result_del is None:
                self.select_ascue()
            else:
                my_list = tk.Text(self.frame_info, width=89, height=28)
                for rows in result_del:
                    for _, value in rows.items():
                        my_list.insert(tk.END, f'{value}   ')
                    my_list.insert(tk.END, '\n')
                    my_list.pack()
                    
    #разлогинится
    def exit_user(self):
        self.authent_OK = False
        self.superadmin_OK = False
        for widget in self.frame_info.winfo_children():
            widget.destroy()
        self.start()

if __name__ == "__main__":
    testObj = Win()
    testObj.mainloop()



