import datetime
import tkinter as tk
from repository import Repo
from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_handler, async_mainloop
import csv
import tkinter.messagebox as mb

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
        self.search_info_fttx = tk.StringVar()
        self.replace_ment = tk.StringVar()
        self.img_fttx_1 = tk.PhotoImage(file='image/fttx_1.png')
        self.img_fttx_2 = tk.PhotoImage(file='image/fttx_2.png')
        self.img_fttx_3 = tk.PhotoImage(file='image/fttx_3.png')
        self.img_fttx_4 = tk.PhotoImage(file='image/fttx_4.png')
        self.img_fttx_5 = tk.PhotoImage(file='image/fttx_5.png')
        self.frame_1 = Frame(self, width=200, height=800)
        self.frame_1.grid(row=0, column=0, rowspan=5, pady=50, sticky=N)
        self.frame_search = Frame(self, width=1020, height=6)
        self.frame_search.grid(row=0, column=1, pady=10, sticky=E)
        self.frame_2 = Label(self, relief=SUNKEN, width=1020, height=700)
        self.frame_2.grid(row=1, column=1, pady=5)
        self.frame_3 = Label(self.frame_2, relief=SUNKEN, background='#e2e2e2', width=1020, height=700)
        self.frame_3.grid(row=1, column=1)
        self.frame_4 = Frame(self.frame_2, relief=SUNKEN, width=500, height=700)
        self.frame_4.grid(row=1, column=1)
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
        self.my_search_city = tk.Label(self.frame_search, text="Быстрый поиск")
        self.my_search_city.grid(row=0, column=1, padx=5)
        self.my_search_city = tk.Entry(self.frame_search, width=30, textvariable=self.search_info_fttx)
        self.my_search_city.delete(0, END)
        self.my_search_city.grid(row=0, column=2, padx=5)
        self.btn_detail_fttx = ttk.Button(self.frame_search, text="поиск FTTX", width=18, command=self.search_fttx)
        self.btn_detail_fttx.grid(row=0, column=10, padx=10)
        self.start()

    # трассы fttx
    @async_handler
    async def fttx_1(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_1, width=1120, height=700)
        label_1.grid(row=0, column=0)

    @async_handler
    async def fttx_2(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_2, width=1120, height=700)
        label_1.grid(row=0, column=0)

    @async_handler
    async def fttx_3(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_3, width=1120, height=700)
        label_1.grid(row=0, column=0)

    @async_handler  #
    async def fttx_4(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_4, width=1120, height=700)
        label_1.grid(row=0, column=0)

    @async_handler
    async def fttx_5(self):
        label_1 = tk.Label(self.frame_2, image=self.img_fttx_5, width=1120, height=700)
        label_1.grid(row=0, column=0)

    @async_handler
    async def start(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_1 = tk.Button(self.frame_2, image=self.img_fttx_1, width=540, height=230, command=self.fttx_1)
        label_1.grid(row=0, column=0, padx=10)
        label_2 = tk.Button(self.frame_2, image=self.img_fttx_2, width=540, height=230, command=self.fttx_2)
        label_2.grid(row=0, column=1, padx=10)
        label_3 = tk.Button(self.frame_2, image=self.img_fttx_3, width=540, height=230, command=self.fttx_3)
        label_3.grid(row=1, column=0, padx=10)
        label_4 = tk.Button(self.frame_2, image=self.img_fttx_4, width=540, height=230, command=self.fttx_4)
        label_4.grid(row=1, column=1, padx=10)
        label_4 = tk.Button(self.frame_2, image=self.img_fttx_5, width=540, height=230, command=self.fttx_5)
        label_4.grid(row=2, column=0, padx=10)

    # блок АСКУЭ
    @async_handler
    async def select_ascue(self):
        res = await Repo.select_ascue_all()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_ascue = tk.Label(self.frame_2, width=1150, text='Город | улица | дом | ip')
        label_ascue.pack()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for row in res:
            my_list.insert(tk.END, f'{row.sity:14} | {row.street:20} | {row.namber:10} | {row.askue:10} \n')
            my_list.insert(tk.END, str('-') * 130)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

    # блок ключей
    @async_handler
    async def select_keys(self):
        res = await Repo.select_keys_all()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_ascue = tk.Label(self.frame_2, width=1150, text='Город | улица | дом | ip')
        label_ascue.pack()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for row in res:
            my_list.insert(tk.END, f'{row.street:14} | {row.home:20} |'
                                   f' {row.entrance:10} | {row.ind:10}| {row.stand:10} \n')
            my_list.insert(tk.END, str('-') * 80)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

    # блок индивидуальные линии БС
    @async_handler
    async def select_ind_bs(self):
        res = await Repo.select_conn_from_base()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for row in res:
            my_list.insert(tk.END, f'{row.sity:14} | {row.bs:7} |'
                                   f' {row.street:15} | {row.namber:10}\n')
            my_list.insert(tk.END, f'{row.comment}\n')
            my_list.insert(tk.END, str('-') * 80)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

        # блок мануал
    @async_handler
    async def select_manual(self):
        res = await Repo.select_man_all()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for row in res:
            my_list.insert(tk.END, f'{row.tip:14} \n')
            my_list.insert(tk.END, f' {row.comment} \n')
            my_list.insert(tk.END, str('-') * 130)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

    # блок Газпром
    @async_handler
    async def select_gazprom(self):
        res = await Repo.select_azs_all()
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.frame_2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
        for row in res:
            my_list.insert(tk.END, f'{row.ip:14} | {row.number:6} |  {row.tip:10}  \n')
            my_list.insert(tk.END, f' {row.region:14} | {row.address} \n')
            my_list.insert(tk.END, f' {row.comment} \n')
            my_list.insert(tk.END, str('-') * 130)
            my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=my_list.yview)

    # блок поиска БС по номеру
    @async_handler
    async def searth_bs(self):
        search_namber = self.searth_bs_namber.get()
        if search_namber is not None:
            self.bs_namber = await Repo.search_bs_number(search_namber)
            self.select_list_bs()
        else:
            self.start()

    @async_handler
    async def searth_address(self):
        searth_bs_address = self.searth_bs_address.get()
        if searth_bs_address is not None:
            self.bs_address = await Repo.search_bs_address(searth_bs_address)
            self.select_list_bs()
        else:
            self.start()

    # блок список базовых
    @async_handler
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
        if bs_namber is not None:
            my_search_bs_label = tk.Label(self.frame_2, width=137, text=str(bs_namber.address))
            my_search_bs_label.pack()
        else:
            my_search_bs_label = tk.Label(self.frame_2, width=137, text=str(' '))
            my_search_bs_label.pack()
        my_search_address = tk.Entry(self.frame_2, width=20, textvariable=self.searth_bs_address)
        my_search_address.pack()
        button_search_address = tk.Button(self.frame_2, text='Поиск по адресу базовой(частичное совпадение)',
                                          command=self.searth_address)
        button_search_address.pack()
        if bs_address is None:
            my_search_bs_label = tk.Label(self.frame_2, width=137, text=str(' '))
            my_search_bs_label.pack()
        else:
            scrollbar = tk.Scrollbar(self.frame_2)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            my_list = tk.Text(self.frame_2, width=138, height=41, wrap=WORD, yscrollcommand=scrollbar.set)
            for row in bs_address:
                my_list.insert(tk.END, f'{row.number:6} | {row.address:50} \n')
                my_list.insert(tk.END, str('-') * 130)
                my_list.insert(tk.END, str('\n'))
            my_list.pack(side=tk.LEFT, fill=tk.BOTH)
            scrollbar.config(command=my_list.yview)

    @async_handler
    async def search_fttx(self):
        temp = self.search_info_fttx.get()
        check_temp = temp.split(", ")
        if len(check_temp) != 3:
            await self.show_warning()
            return
        res = await Repo.select_all_info(temp)
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_mkn_16 = tk.Label(self.frame_2, width=1020, text='МКН-16, МКН-17,МКН-19 --  ЖЭУ-25 | Телефон: 33-73-52,\n'
                                                               'кластер Аэродром | ЖЭУ-25 | Телефон: 33-73-52'
                                                               '\nНовополесская 2, Новополесская 4 | ЖЭУ-8 | '
                                                               'Телефон: 21-72-10')
        label_mkn_16.pack()
        my_list = tk.Text(self.frame_2, width=138, height=37, wrap=WORD)
        my_list.insert(tk.END, f'{res.sity:14} | {res.claster:14} | {res.street:15} | '
                               f' {res.namber:6} |{res.comment} \n')

        my_list.insert(tk.END, str('-') * 130)
        my_list.insert(tk.END, str('\n'))
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)

    #некореектный ввод быстрый поиск
    async def show_warning(self):
        msg = "Введены некорректные данные "
        mb.showwarning("Предупреждение", msg)

    # блок кластер_info
    @async_handler
    async def detail_fttx(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        name_claster = tk.Label(self.frame_2, text="Список кластеров")
        name_claster.grid(row=0, column=0, padx=220)
        self.list_claster = ttk.Combobox(self.frame_2, width=50, values=[
                                                                         "МКН16",
                                                                         "МКН17",
                                                                         "МКН19",
                                                                         "Аэродром",
                                                                          ], state="readonly")
        self.list_claster.grid(row=1, column=0)
        search_claster = Button(self.frame_2, text="Поиск по кластерам", command=self.search_claster)
        search_claster.grid(row=2, column=0)
        name_street = tk.Label(self.frame_2, text="Список улиц")
        name_street.grid(row=0, column=1, padx=220)
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
        self.list_street.grid(row=1, column=1)
        search_street = Button(self.frame_2, text="Поиск по улицам", command=self.result_street)
        search_street.grid(row=2, column=1)
        my_list = tk.Text(self.frame_2, width=138, height=33)
        my_list.grid(columnspan=2)

    @async_handler
    async def search_claster(self):
        claster = self.list_claster.get()
        result = await Repo.select_claster(claster)
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_mkn_16 = tk.Label(self.frame_2, width=1020, text='МКН-16, МКН-17,МКН-19 --  ЖЭУ-25 | Телефон: 33-73-52,\n'
                                                               'кластер Аэродром | ЖЭУ-25 | Телефон: 33-73-52'
                                                               '\nНовополесская 2, Новополесская 4 | ЖЭУ-8 | '
                                                               'Телефон: 21-72-10')
        label_mkn_16.pack()
        if result is None:
            my_search_bs_label = tk.Label(self.frame_2, width=137, text=str(' '))
            my_search_bs_label.pack()
        else:
            scrollbar = tk.Scrollbar(self.frame_2)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            my_list = tk.Text(self.frame_2, width=138, height=34, wrap=WORD, yscrollcommand=scrollbar.set)
            for row in result:
                my_list.insert(tk.END, f'{row.id:4} | {row.sity:10} | {row.claster:8} | {row.street:15} | '
                               f' {row.namber:6} | {row.comment} \n')
                my_list.insert(tk.END, str('-') * 130)
                my_list.insert(tk.END, str('\n'))
            scrollbar.config(command=my_list.yview)
            my_list.pack(side=tk.LEFT, fill=tk.BOTH)

    @async_handler
    async def result_street(self):
        street = self.list_street.get()
        result = await Repo.select_street(street)
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        label_mkn_16 = tk.Label(self.frame_2, width=1020, text='МКН-16, МКН-17,МКН-19 --  ЖЭУ-25 | Телефон: 33-73-52,\n'
                                                               'кластер Аэродром | ЖЭУ-25 | Телефон: 33-73-52'
                                                               '\nНовополесская 2, Новополесская 4 | ЖЭУ-8 | '
                                                               'Телефон: 21-72-10')
        label_mkn_16.pack()
        if result is None:
            my_search_bs_label = tk.Label(self.frame_2, width=137, text=str(' '))
            my_search_bs_label.pack()
        else:
            scrollbar = tk.Scrollbar(self.frame_2)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            my_list = tk.Text(self.frame_2, width=138, height=34, wrap=WORD, yscrollcommand=scrollbar.set)
            for row in result:
                my_list.insert(tk.END, f'{row.id:4} | {row.sity:10} | {row.claster:8} | {row.street:15} | '
                                       f' {row.namber:6} | {row.comment} \n')
                my_list.insert(tk.END, str('-') * 130)
                my_list.insert(tk.END, str('\n'))
            my_list.pack(side=tk.LEFT, fill=tk.BOTH)
            scrollbar.config(command=my_list.yview)
            my_list.pack(side=tk.LEFT, fill=tk.BOTH)

    # импорт данных реестр
    @async_handler
    async def data_import(self):
        requests = self.requests.get()
        requests_all = requests.split(',')
        if len(requests_all) != 12:
            await self.show_warning()
            return
        await Repo.insert_user_info(requests_all)
        self.start_import()

    # Обновление информации по адресам fttx
    @async_handler
    async def update_info_fttx(self):
        update_baza = self.update_baza.get()
        update_baza = update_baza.split(', ', 1)
        ssid = update_baza[0]
        value = update_baza[1]
        await Repo.update_info_fttx(ssid, value)
        self.start_import()

    # экспорт данных в .csv по замене оборудования
    @async_handler
    async def support_csv_export(self):
        result = await Repo.csv_export_fttx()
        today = datetime.date.today()
        with open(f'Замена_оборудования_{today}.csv', 'w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL, lineterminator="\r")
            for row in result:
                csv_writer.writerow([row.id, row.date, row.address, row.equipment, row.problem, row.responsible])
        self.start_import()

    # импорт в replacement данных по замене оборудования
    @async_handler
    async def replacement(self):
        replace_ment = self.replace_ment.get()
        replace_ment_all = replace_ment.split(';')
        if len(replace_ment_all) != 6:
            await self.show_warning()
            return
        await Repo.insert_into_replacement(replace_ment_all)
        self.start_import()

    # экспорт данных в .csv основной отчёт
    @async_handler
    async def csv_export(self):
        date_1 = self.date_1.get()
        date_2 = self.date_2.get()
        if (date_1 is None or date_2 is None
                or len(date_1.split('-')) != 3 or len(date_2.split('-')) != 3):
            self.start()
        else:
            for widget in self.frame_2.winfo_children():
                widget.update()
        result = await Repo.csv_export_fttx_users(date_1, date_2)
        with open(f'отчёт_{date_1}--{date_2}.csv', 'w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL, lineterminator="\r")
            for row in result:
                csv_writer.writerow([row.id, row.reestr, row.date, row.sity, row.street, row.home, row.apartment,
                                     row.name, row.cable_1, row.cable_2, row.cable_3, row.connector])
            self.start_import()

    # блок статистики (количество абонов + метраж) по датам
    @async_handler
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
            street = await Repo.csv_export_fttx_users(date_3, date_4)
            dict_subscriber = dict()
            query_sum_cable = 0
            for row in street:
                list_lenght.append(row.street)
                dict_subscriber[row.street] = dict_subscriber.get(row.street, 0) + 1
                query_sum_cable += row.cable_1 + row.cable_2 + row.cable_3
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
    @async_handler
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
        result = await Repo.select_users()
        my_label = tk.Text(self.frame_2, width=138, height=6)
        for row in result:
            my_label.insert(tk.END, (f"{row.id:6} | {row.date} | {row.sity.strip():12} | {row.street.strip():16} |"
                                     f" {row.home.strip():6} | {row.apartment:5} | {row.name.strip():36} | "
                                     f" {row.cable_1:4} | {row.cable_2:4} | {row.cable_3:4} | {row.connector:2}"))
            my_label.insert(tk.END, '\n')
        my_label.pack()
        frame_3 = Label(self.frame_2, width=1020, height=700)
        frame_3.pack(anchor=NW)
        my_date_1 = tk.Entry(frame_3, width=10, textvariable=self.date_1)
        my_date_1.grid(row=0, column=0, padx=10, pady=5)
        my_date_2 = tk.Entry(frame_3, width=10, textvariable=self.date_2)
        my_date_2.grid(row=1, column=0, padx=10, pady=5)
        button_send_date = tk.Button(frame_3, text='Сформировать отчёт fttx\nYYYY-MM-DD', command=self.csv_export)
        button_send_date.grid(row=2, column=0, padx=70, pady=5)
        button_send_support = tk.Button(frame_3, text='Сформировать отчёт\nзамена оборудования',
                                        command=self.support_csv_export)
        button_send_support.grid(row=2, column=1, padx=100, pady=5)
        my_date_3 = tk.Entry(frame_3, width=10, textvariable=self.date_3)
        my_date_3.grid(row=0, column=2, padx=10, pady=5)
        my_date_4 = tk.Entry(frame_3, width=10, textvariable=self.date_4)
        my_date_4.grid(row=1, column=2, padx=10, pady=5)
        button_send = tk.Button(frame_3, text='Статистика по абонам\nYYYY-MM-DD', command=self.statistic)
        button_send.grid(row=2, column=2, padx=120, pady=5)
        my_enter_replacement = tk.Label(self.frame_2, width=110,
                                        text='Добавить запись (YYYY-MM-DD, адрес, тип оборудования, проблема, кому передано), '
                                             'разделитель  \";\" ')
        my_enter_replacement.pack()
        my_replacement = tk.Entry(self.frame_2, width=110, textvariable=self.replace_ment)

        my_replacement.pack(pady=5)
        button_send_replacement = tk.Button(self.frame_2, text='Добавить запись', command=self.replacement)
        button_send_replacement.pack(pady=5)
        result = await Repo.select_replacement()    # выборка последних 10 записей по оборудованию
        my_label = tk.Text(self.frame_2, width=138, height=6)
        for row in result:
            my_label.insert(tk.END, (f"{row.id:6} | {row.date} | {row.address.strip():34} |"
                                     f" {row.equipment:14} | {row.problem} | {row.responsible} "
                                     ))
            my_label.insert(tk.END, '\n')
        my_label.pack()
        my_enter_update_baza = tk.Label(self.frame_2, width=110, text='Обновить запись основной базы( ID, comment ),'
                                                                      'разделитель, первая \", \"')
        my_enter_update_baza.pack()
        my_update_baza = tk.Entry(self.frame_2, width=110, textvariable=self.update_baza)
        my_update_baza.delete('0', tk.END)
        my_update_baza.pack(pady=5)
        button_send_update_baza = tk.Button(self.frame_2, text='Обновить запись', command=self.update_info_fttx)
        button_send_update_baza.pack(pady=5)


if __name__ == "__main__":
    testObj = Win()
    async_mainloop(testObj)  # <--- запуск асинхронно
