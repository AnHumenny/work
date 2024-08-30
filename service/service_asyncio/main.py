import tkinter as tk

import func
from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_handler, async_mainloop
import csv
from mysql.connector import connect
dtb = func.Auth_Mysql(host=func.host, port=func.port, user=func.user,
                      password=func.password, dtb=func.dtb)


class Win(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title('FTTX/WTTX Гомель')
        self.geometry('1300x800')
        self.searth_bs_namber = tk.StringVar()
        self.searth_bs_address = tk.StringVar()
        self.list_claster = tk.StringVar()
        self.list_street = tk.Scrollbar()
        self.bs_address = None
        self.bs_namber = None
        self.update_info = tk.StringVar()
        self.requests = tk.StringVar()
        self.update_baza = tk.StringVar()
        self.date_1 = tk.StringVar()
        self.date_2 = tk.StringVar()
        self.date_3 = tk.StringVar()
        self.date_4 = tk.StringVar()
        self.replace_ment = tk.StringVar()
        self.img_fttx_1 = tk.PhotoImage(file='image/fttx_1.png')
        self.img_fttx_2 = tk.PhotoImage(file='image/fttx_2.png')
        self.img_fttx_3 = tk.PhotoImage(file='image/fttx_3.png')
        self.img_fttx_4 = tk.PhotoImage(file='image/fttx_4.png')
        self.img_fttx_5 = tk.PhotoImage(file='image/fttx_5.png')
        self.frame_1 = Frame(self, width=200, height=800)
        self.frame_1.pack(side=LEFT)
        self.frame_2 = Label(self, relief=SUNKEN, background='#e2e2e2', width=1020, height=700)
        self.frame_2.pack(anchor=N, ipadx=50, ipady=50)
        self.frame_3 = Label(self.frame_2, relief=SUNKEN, background='#e2e2e2', width=1020, height=700)
        self.frame_3.pack(anchor=NW)
        self.frame_4 = Frame(self.frame_2, relief=SUNKEN, width=500, height=700)
        self.frame_4.pack()
        self.menu = Label(self.frame_1)
        self.menu.pack(anchor=NW)
        self.btn_askue = ttk.Button(self.menu, text="Трассы", width=18, command=self.start)
        self.btn_askue.grid(row=0, column=0, padx=20)
        self.btn_askue = ttk.Button(self.menu, text="АСКУЭ", width=18, command=self.select_ascue)
        self.btn_askue.grid(row=1, column=0, padx=20)
        self.btn_gazprom = ttk.Button(self.menu, text="Газпром", width=18, command=self.select_gazprom)
        self.btn_gazprom.grid(row=2, column=0, padx=20)
        self.btn_keys = ttk.Button(self.menu, text="Ключи", width=18, command=self.select_keys)
        self.btn_keys.grid(row=3, column=0, padx=20)
        self.btn_manual = ttk.Button(self.menu, text="Мануал", width=18, command=self.select_manual)
        self.btn_manual.grid(row=4, column=0, padx=20)
        self.btn_bs = ttk.Button(self.menu, text="Инд. линии БС", width=18, command=self.select_ind_bs)
        self.btn_bs.grid(row=5, column=0, padx=20)
        self.btn_list_bs = ttk.Button(self.menu, text="Список БС", width=18, command=self.select_list_bs)
        self.btn_list_bs.grid(row=6, column=0, padx=20)
        self.btn_list_info = ttk.Button(self.menu, text="Инфо", width=18, command=self.start_import)
        self.btn_list_info.grid(row=7, column=0, padx=20)
        self.btn_list_claster = Label(self.menu, text="--------------")
        self.btn_list_claster.grid(row=8, column=0, padx=20)
        self.btn_detail_fttx = ttk.Button(self.menu, text="info FTTX", width=18, command=self.detail_fttx)
        self.btn_detail_fttx.grid(row=13, column=0, padx=20)

        self.start()

    # трассы fttx
    @async_handler  # <--- Добавить декоратор
    async def fttx_1(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_1, width=1150, height=700)
        label_1.grid(row=0, column=0)

    @async_handler  # <--- Добавить декоратор
    async def fttx_2(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_2, width=1150, height=700)
        label_1.grid(row=0, column=0)

    @async_handler  # <--- Добавить декоратор
    async def fttx_3(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_3, width=1150, height=700)
        label_1.grid(row=0, column=0)

    @async_handler  # <--- Добавить декоратор
    async def fttx_4(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_4, width=1150, height=700)
        label_1.grid(row=0, column=0)

    @async_handler  # <--- Добавить декоратор
    async def fttx_5(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_5, width=1150, height=700)
        label_1.grid(row=0, column=0)

    @async_handler  # <--- Добавить декоратор
    async def start(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_1 = tk.Button(self.frame_2, image=self.img_fttx_1, width=550, height=235, command=self.fttx_1)
        label_1.grid(row=0, column=0, padx=10)
        label_2 = tk.Button(self.frame_2, image=self.img_fttx_2, width=550, height=235, command=self.fttx_2)
        label_2.grid(row=0, column=1, padx=10)
        label_3 = tk.Button(self.frame_2, image=self.img_fttx_3, width=550, height=235, command=self.fttx_3)
        label_3.grid(row=1, column=0, padx=10)
        label_4 = tk.Button(self.frame_2, image=self.img_fttx_4, width=550, height=235, command=self.fttx_4)
        label_4.grid(row=1, column=1, padx=10)
        label_4 = tk.Button(self.frame_2, image=self.img_fttx_5, width=550, height=235, command=self.fttx_5)
        label_4.grid(row=2, column=0, padx=10)

    # блок АСКУЭ
    @async_handler  # <--- Добавить декоратор
    async def select_ascue(self):
        res = dtb.select_ascue()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_ascue = tk.Label(self.frame_2, width=1150, text='Город | улица | дом | ip')
        label_ascue.pack()
        self.res_ascue_keys_ind(res)

    # блок ключей
    @async_handler  # <--- Добавить декоратор
    async def select_keys(self):
        res = dtb.select_keys()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_keys = tk.Label(self.frame_2, width=1150, text='ID | улица | дом | количество подьездов | '
                                                             'индивидуальный ключ | стандартный ключ')
        label_keys.pack()
        self.res_ascue_keys_ind(res)

    # блок индивидуальные линии БС
    @async_handler  # <--- Добавить декоратор
    async def select_ind_bs(self):
        res = dtb.select_ind_bs()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        self.res_ascue_keys_ind(res)

    # Обобщённо АСКУЭ, ключи, индивидуалные линии БС
    @async_handler  # <--- Добавить декоратор
    async def res_ascue_keys_ind(self, res):
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for rows in res:
            for _, value in rows.items():
                my_list.insert(tk.END, f'{str(value):20}')
            my_list.insert(tk.END, str('\n'))
            my_list.insert(tk.END, str('-') * 120)
            my_list.insert(tk.END, str('\n'))
            my_list.pack(side=tk.LEFT, fill=tk.BOTH)
            scrollbar.config(command=my_list.yview)

        # блок мануал
    @async_handler  # <--- Добавить декоратор
    async def select_manual(self):
        res = dtb.select_manual()
        self.res_man(res)
        # блок мануал результат

    @async_handler  # <--- Добавить декоратор
    async def res_man(self, res):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for rows in res:
            for _, value in rows.items():
                my_list.insert(tk.END, f'({value})')
                my_list.insert(tk.END, str('\n'))
            my_list.insert(tk.END, str('-') * 80)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

    # блок Газпром
    @async_handler  # <--- Добавить декоратор
    async def select_gazprom(self):
        res = dtb.select_gazprom()
        self.select_gazprom_man(res)

        # блок газпром результат
    @async_handler  # <--- Добавить декоратор
    async def select_gazprom_man(self, res):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for rows in res:
            result = {v: k for k, v in rows.items()}
            res = ', '.join(str(value) for value in result if value is not None)
            my_list.insert(tk.END, f'{res:10}')
            my_list.insert(tk.END, str('\n'))
            my_list.insert(tk.END, str('-') * 80)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

    # блок поиска БС по номеру
    @async_handler  # <--- Добавить декоратор
    async def searth_bs(self):
        searth_namber = self.searth_bs_namber.get()
        if searth_namber != '':
            self.bs_namber = dtb.searth_bs_namber(searth_namber)
            self.select_list_bs()
        else:
            self.start()

    @async_handler  # <--- Добавить декоратор
    async def searth_address(self):
        searth_bs_address = self.searth_bs_address.get()
        if searth_bs_address != '':
            self.bs_address = dtb.search_bs_address(searth_bs_address)
            self.select_list_bs()
        else:
            self.start()

    # блок список базовых
    @async_handler  # <--- Добавить декоратор
    async def select_list_bs(self):
        bs_namber = self.bs_namber
        bs_address = self.bs_address
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        my_search_bs_label = tk.Label(self.frame_2, width=137, text='')
        my_search_bs_label.pack()
        my_search_bs = tk.Entry(self.frame_2, width=10, textvariable=self.searth_bs_namber)
        my_search_bs.pack()
        button_search_bs = tk.Button(self.frame_2, text='Поиск по номеру базовой', command=self.searth_bs)
        button_search_bs.pack()
        my_search_bs_label = tk.Label(self.frame_2, width=137, text=str(bs_namber))
        my_search_bs_label.pack()
        my_search_address = tk.Entry(self.frame_2, width=20, textvariable=self.searth_bs_address)
        my_search_address.pack()
        button_search_address = tk.Button(self.frame_2, text='Поиск по адресу базовой(частичное совпадение)',
                                          command=self.searth_address)
        button_search_address.pack()
        my_label_addr = tk.Text(self.frame_2, width=138, height=41, wrap=WORD)
        for rows in bs_address:
            # for rows in res:
            res_street_bs = {v: k for k, v in rows.items()}
            value = ', '.join(str(value) for value in res_street_bs if value is not None)
            my_label_addr.insert(tk.END, f'{value:20}')
            my_label_addr.insert(tk.END, str('  '))
            my_label_addr.insert(tk.END, str('\n'))
            my_label_addr.pack(side=tk.LEFT, fill=tk.BOTH)

    # блок кластер_info
    @async_handler  # <--- Добавить декоратор
    async def detail_fttx(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        name_claster = tk.Label(self.frame_2, text="Список кластеров")
        name_claster.pack(pady=10)
        self.list_claster = ttk.Combobox(self.frame_2, width=50, values=[
                                                                         "МКН16",
                                                                         "МКН17",
                                                                         "МКН19",
                                                                         "Аэродром",
                                                                          ], state="readonly")
        self.list_claster.pack()
        search_claster = Button(self.frame_2, text="Поиск по кластерам", command=self.search_claster)
        search_claster.pack(pady=20)
        name_street = tk.Label(self.frame_2, text="Список улиц")
        name_street.pack(pady=5)
        self.list_street = ttk.Combobox(self.frame_2, width=50, values=[
                                                                     "Мазурова",
                                                                     "Головацкого",
                                                                     "Хатаевича",
                                                                     "Бородина",
                                                                     "Кожара",
                                                                     "Новополесская",
                                                                     "Старочерниговская",
                                                                     "Телегина",
                                                                      ], state="readonly")
        self.list_street.pack(pady=10)
        search_street = Button(self.frame_2, text="Поиск по улицам", command=self.result_street)
        search_street.pack()


    @async_handler  # <--- Добавить декоратор
    async def search_claster(self):
        claster = self.list_claster.get()
        print("кластер", claster)
        res = dtb.select_claster(claster)
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_mkn_16 = tk.Label(self.frame_2, width=1020, text='МКН-16, МКН-17,МКН-19 --  ЖЭУ-25 | Телефон: 33-73-52,\n'
                                                               'кластер Аэродром | ЖЭУ-25 | Телефон: 33-73-52'
                                                               '\nНовополесская 2, Новополесская 4 | ЖЭУ-8 | '
                                                               'Телефон: 21-72-10')
        label_mkn_16.pack()
        scrollbar = tk.Scrollbar(self.frame_2)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for rows in res:
            res_mkn = {v: k for k, v in rows.items()}
            value = ', '.join(str(value) for value in res_mkn if value is not None)
            my_list.insert(tk.END, value)
            my_list.insert(tk.END, str('  '))
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=my_list.yview)


    @async_handler  # <--- Добавить декоратор
    async def result_street(self):
        street = self.list_street.get()
        print("стрит", street)
        res = dtb.select_street(street)
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_info = tk.Label(self.frame_2, width=1020, text='МКН-16, МКН-17,МКН-19 --  ЖЭУ-25 | Телефон: 33-73-52,\n'
                                                             'кластер Аэродром | ЖЭУ-25 | Телефон: 33-73-52'
                                                             '\nНовополесская 2, Новополесская 4 | ЖЭУ-8 | '
                                                             'Телефон: 21-72-10')
        label_info.pack()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for rows in res:
            res_street = {v: k for k, v in rows.items()}
            value = ', '.join(str(value) for value in res_street if value is not None)
            my_list.insert(tk.END, value)
            my_list.insert(tk.END, str('  '))
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=my_list.yview)

    # Обновление информации по адресам fttx
    @async_handler  # <--- Добавить декоратор
    async def update_info_fttx(self):
        update_baza = self.update_baza.get()
        update_baza = update_baza.split(', ', 1)
        ssid = update_baza[0]
        comment = update_baza[1]
        dtb.update_info(comment, ssid)
        self.start_import()

    # импорт данных реестр (+ выборка десять последних)
    @async_handler  # <--- Добавить декоратор
    async def data_import(self):
        requests = self.requests.get()
        requests_all = requests.split(',')
        reestr = requests_all[0]
        date = requests_all[1]
        sity = requests_all[2]
        street = requests_all[3]
        home = requests_all[4]
        apartment = requests_all[5]
        name = requests_all[6]
        cable_1 = requests_all[7]
        cable_2 = requests_all[8]
        cable_3 = requests_all[9]
        connector = requests_all[10]
        dtb.insert_reestr(reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector)
        self.start_import()

    # экспорт данных в .csv по замене оборудования
    @async_handler  # <--- Добавить декоратор
    async def support_csv_export(self):
        result = dtb.csv_export_replacement()

        with open('Замена_оборудования.csv', 'w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL, lineterminator="\r")
            for rows in result:
                result = {v: k for k, v in rows.items()}
                res = ', '.join(str(value) for value in result if value is not None)
                csv_writer.writerow([res])
        self.start_import()

    # экспорт данных в .csv основной отчёт
    @async_handler  # <--- Добавить декоратор
    async def csv_export(self):
        date_1 = self.date_1.get()
        date_2 = self.date_2.get()
        if (date_1 == '' or date_2 == ''
                or len(date_1.split('-')) != 3 or len(date_2.split('-')) != 3):
            self.start()
        else:
            for widget in self.frame_2.winfo_children():
                widget.update()

        result = dtb.csv_export_fttx(date_1, date_2)

        with open(f'отчёт_{date_1}--{date_2}.csv', 'w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL, lineterminator="\r")
            for rows in result:
                result = {v: k for k, v in rows.items()}
                res = ', '.join(str(value) for value in result if value is not None)
                csv_writer.writerow([res])
            self.start_import()

    # блок статистики (количество абонов + метраж) по датам
    @async_handler  # <--- Добавить декоратор
    async def statistic(self):
        date_3 = self.date_3.get()
        date_4 = self.date_4.get()
        if (date_3 == '' or date_4 == ''
                or len(date_3.split('-')) != 3 or len(date_4.split('-')) != 3):
            self.start()
        else:

            for widgets in self.frame_2.winfo_children():
                widgets.destroy()
            list_lenght = []
            result = dtb.select_all_people(date_3, date_4)
            dict_subscriber = dict()
            for rows in result:
                res_eq = {v: k for k, v in rows.items()}
                for row in res_eq:
                    list_lenght.append(row)
                    dict_subscriber[row] = dict_subscriber.get(row, 0) + 1
                print(list_lenght, dict_subscriber)
            sum_cable = dtb.query_sum(date_3, date_4)
            print('итоговая сумма', sum_cable)
            query_sum_cable = int(sum_cable)
            my_label_empty = tk.Label(self.frame_2, width=300, anchor=NW, padx=40, pady=10)
            my_label_empty.pack(side=TOP)
            if int(query_sum_cable) > 0:
                my_label_21 = tk.Label(self.frame_2, width=300, anchor=NW, padx=40)
                my_label_21["text"] = 'За', 'период', 'с', date_3, 'по', date_4
                my_label_21.pack()
                my_label_11 = tk.Label(self.frame_2, width=300, anchor=NW, padx=40)
                my_label_11["text"] = 'Всего', len(list_lenght), 'абонентов'
                my_label_11.pack()
                my_label_8 = tk.Label(self.frame_2, width=300, anchor=NW, padx=40)
                my_label_8["text"] = 'Общий', 'метраж', 'кабеля:', query_sum_cable, 'метра(ов)'
                my_label_8.pack()
                my_label_8_1 = tk.Label(self.frame_2, width=300, anchor=NW, padx=40)
                my_label_8_1["text"] = '-' * 30
                my_label_8_1.pack()
                for key, value in dict_subscriber.items():
                    my_label_1 = tk.Label(self.frame_2, width=300, anchor=NW, padx=20)
                    my_label_1["text"] = key, value, 'абонента(ов)'
                    my_label_1.pack()
            button_back = tk.Button(self.frame_2, text='Вернутся\n на ИНФО', command=self.start_import)
            button_back.pack()

    # раздел Инфо
    @async_handler  # <--- Добавить декоратор
    async def start_import(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        my_enter = tk.Label(self.frame_2, width=125,
                            text='Добавить запись (номер реестра, YYYY-MM-DD, город, улица, дом, квартира,'
                                 ' ФИО, кабель, кабель, кабель, коннектор), разделитель - ","')
        my_enter.pack(pady=10)
        my_list = tk.Entry(self.frame_2, width=110, textvariable=self.requests)
        my_list.pack(pady=5)
        button_send_col = tk.Button(self.frame_2, text='Добавить запись', command=self.data_import)
        button_send_col.pack(pady=5)
        conn = connect(host=func.host,
                       user=func.user,
                       password=func.password,
                       database=func.dtb
                       )
        cursor = conn.cursor()
        query = 'SELECT id, reestr, date, sity, street, home, apartment, name FROM info ORDER BY id DESC LIMIT 20'
        cursor.execute(query)
        result = cursor.fetchall()
        my_label = tk.Text(self.frame_2, width=138, height=7)
        for rows in result:
            for row in rows:
                my_label.insert(tk.END, row)
                my_label.insert(tk.END, '  ')
            my_label.insert(tk.END, '\n')
        my_label.pack()

        conn.close()

        frame_3 = Label(self.frame_2, width=1020, height=700)
        frame_3.pack(anchor=NW)
        my_date_1 = tk.Entry(frame_3, width=10, textvariable=self.date_1)
        my_date_1.grid(row=0, column=0, padx=10, pady=7)
        my_date_2 = tk.Entry(frame_3, width=10, textvariable=self.date_2)
        my_date_2.grid(row=1, column=0, padx=10, pady=7)
        button_send_date = tk.Button(frame_3, text='Сформировать отчёт fttx\nYYYY-MM-DD', command=self.csv_export)
        button_send_date.grid(row=2, column=0, padx=70, pady=7)
        button_send_update = tk.Button(frame_3, text='Обновить',
                                       command=self.start_import)
        button_send_update.grid(row=1, column=1, padx=100, pady=7)
        button_send_support = tk.Button(frame_3, text='Сформировать отчёт\nзамена оборудования',
                                        command=self.support_csv_export)
        button_send_support.grid(row=2, column=1, padx=100, pady=7)
        my_date_3 = tk.Entry(frame_3, width=10, textvariable=self.date_3)
        my_date_3.grid(row=0, column=2, padx=10, pady=7)
        my_date_4 = tk.Entry(frame_3, width=10, textvariable=self.date_4)
        my_date_4.grid(row=1, column=2, padx=10, pady=7)
        button_send = tk.Button(frame_3, text='Статистика по абонам\nYYYY-MM-DD', command=self.statistic)
        button_send.grid(row=2, column=2, padx=120, pady=7)
        my_enter_replacement = tk.Label(self.frame_2, width=110,
                                        text='Добавить запись (YYYY-MM-DD, адрес, тип оборудования, проблема, кому передано), '
                                             'разделитель  \";\" ')
        my_enter_replacement.pack()
        my_replacement = tk.Entry(self.frame_2, width=110, textvariable=self.replace_ment)
        my_replacement.pack(pady=5)
        button_send_replacement = tk.Button(self.frame_2, text='Добавить запись', command=self.replacement)
        button_send_replacement.pack(pady=5)
        # выборка последних 10 записей по оборудованию

        conn = connect(host=func.host,
                       user=func.user,
                       password=func.password,
                       database=func.dtb
                       )
        cursor = conn.cursor()
        query = 'SELECT * FROM replacement ORDER BY id DESC LIMIT 10'
        cursor.execute(query)
        result = cursor.fetchall()

        my_label_rep = tk.Text(self.frame_2, width=138, height=7)
        for rows in result:
            for row in rows:
                my_label_rep.insert(tk.END, row)
                my_label_rep.insert(tk.END, '  ')
            my_label_rep.insert(tk.END, '\n')
        my_label_rep.pack()
        my_enter_update_baza = tk.Label(self.frame_2, width=110, text='Обновить запись основной базы( ID, comment ),'
                                                                      'разделитель, первая \", \"')
        my_enter_update_baza.pack()
        my_update_baza = tk.Entry(self.frame_2, width=110, textvariable=self.update_baza)
        my_update_baza.delete('0', tk.END)
        my_update_baza.pack(pady=5)
        button_send_update_baza = tk.Button(self.frame_2, text='Обновить запись', command=self.update_info_fttx)
        button_send_update_baza.pack(pady=5)

    # импорт в replacement данных по замене оборудования
    @async_handler  # <--- Добавить декоратор
    async def replacement(self):
        replace_ment = self.replace_ment.get()
        replace_ment_all = replace_ment.split(';')
        date = replace_ment_all[0]
        address = replace_ment_all[1]
        equipment = replace_ment_all[2]
        problem = replace_ment_all[3]
        responsible = replace_ment_all[4]
        dtb.insert_replacement(date, address, equipment, problem, responsible)
        self.start_import()

if __name__ == "__main__":
    testObj = Win()
    async_mainloop(testObj)  # <--- запуск асинхронно