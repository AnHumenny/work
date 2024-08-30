from aiogram import types, F, Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import as_list
from aiogram.utils.keyboard import InlineKeyboardBuilder
import base64
import list
import config
import conf
from aiogram.fsm.state import StatesGroup, State
import keyboards
import time

dtb = config.telega_SQL(host=config.host, port=config.port, user=config.user,
                        password=config.password, dtb=config.dtb)
dtbs = conf.Postgre_bot(host=conf.host, port=conf.port, user=conf.user,
                        password=conf.password, database=conf.database)


router = Router()
class Select_Info(StatesGroup):
    choosing_user_name = State()
    choosing_address = State()
    register_user = State()
    add_info = State()
    view_eqiup = State()
    del_eqiup = State()
    view_address = State()
    view_user = State()
    view_bs = State()
    view_address_bs = State()
    delete_ascue = State()
    add_new_info = State()
    view_azs = State()

class Registred:
    admin_OK = False
    user_OK = False
    available_user_names = []
    login = ''

named_tuple = time.localtime()  # получаем struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M", named_tuple)

@router.message(StateFilter(None), Command("start"))
async def start_handler(msg: Message, state=FSMContext):
    await msg.answer("Привет! \n")
    await msg.answer(
        text="Знаешь как зайти? :)",
        reply_markup=keyboards.make_row_keyboard(['xxxxx'])
    )
    await state.set_state(Select_Info.register_user)  # ожидание выбора на виртуальной клавиатуре
#ввод и проверка пароля
@router.message(Select_Info.register_user)
async def cmd_auth(msg: Message, state: FSMContext):
    bot = Bot(token=config.API_TOKEN)
    print('это msg.text', msg.text)
    autent = msg.text.split('|')
    print(len(autent))
    if len(autent) != 4:
        await msg.answer(
            text=f"Короткий пароль ;("
        )       
        await state.clear()
    else:
        auth = msg.text.split("|")
        login = auth[0]
        pswrd = auth[1]
        pass_wrd = pswrd.encode('utf-8')
        password = base64.b64encode(pass_wrd)
        if len(login) == 0 or len(password) < 7:
            await msg.answer(
                text=f"Что то не получилось с паролем :("
            )
            await state.clear()
            return
        else:
            result = dtb.select_pass(login, password)
            if result is None:
                 await msg.answer(
                    text=f"Не зашло с паролем :("    
                    )
                 await state.clear()    
            else:     
                for row in result:
                    login = row.get('login')
                    name = row.get('name')
                    print(name)
                    my_pass = row.get('password')
                    user = msg.from_user.full_name
                    print(user)
                    content = list.bot_log[0]
                    time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                    dtbs.insert_entr(user, content, time_str)
                    dtb.fix_time(user, time_string)
                    print(Registred.admin_OK)
                    if login in list.log_admin:
                        Registred.admin_OK = True                   
                        await msg.answer(
                            text=f"Набери\n/help, {login}"
                            )
                        print('name = ', msg.from_user.full_name)
                        for row in list.log_admin:
                            if login in row: 
                                Registred.admin_OK = True
                                await bot.send_message("#send to my ID", 'В бот зашёл ' + msg.from_user.first_name)  #ошибка незакрытой сессии!!!                    
                            await state.clear()

#мануал
@router.message(F.text, Command("help"))
async def cmd_help(msg: Message):    
    if (msg.from_user.id not in list.id_admin
            and Registred.admin_OK is False):    #проверка админа
        await msg.answer(
            text=f"Увы. Нет доступа к внутренней информации :("
        )
        return
    else:
        content = as_list(*list.help)
        content_adm = as_list(*list.adm_help)
        await msg.answer(**content.as_kwargs())
        await msg.answer(**content_adm.as_kwargs())
            
#юридический адрес организации
@router.message(F.text, Command("address"))
async def message_handler(msg: Message):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        content = as_list("юр. адрес")
        await msg.reply(**content.as_kwargs())

#список контактов по МТС
@router.message(F.text, Command('contact'))
async def message_handler(msg: Message):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        content = as_list(*list.mts)
        await msg.answer(**content.as_kwargs())
#Общий список
@router.message(F.text, Command("employees"))
async def cmd_advanced_example(msg: Message):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        group_fiks = dtb.group_fiks()  # короткий список (Имя + телефон)
        try:
            for rows in group_fiks:
                for _, value in rows.items():
                    content = as_list(value)
                    await msg.answer(**content.as_kwargs())
        except AttributeError:
            print('Пустой запрос')         

#ветка диалога /info, возврат в основную после каждого запроса
@router.message(StateFilter(None), Command("info"))
async def cmd_user(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        # формируем список сотрудников из БД, подробно
        group_mont = dtb.group_mont()
        for rows in group_mont:
            for _, value in rows.items():
                Registred.available_user_names.append(value)
        await msg.answer(
            text="Кто интересует (пример ниже)",
            reply_markup=keyboards.make_row_keyboard(list.available_user_names)       #выборка из БД (сотрудники)
            )
        await state.set_state(Select_Info.choosing_user_name)  #ожидание выбора на виртуальной клавиатуре
@router.message(Select_Info.choosing_user_name, F.text.in_(Registred.available_user_names))  #класс + переменная, текст в переменной
async def select_user(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        user = msg.from_user.full_name
        content = list.bot_log[1] + ' в '
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        dtbs.insert_entr(user, content, time_str)
        name = msg.text
        info_user = dtb.select_user(name)         #запрос по конкретному лицу
        if info_user is False:
            await msg.answer(
                f"Нет такого :(",
                reply_markup=types.ReplyKeyboardRemove()  # убираем клавиатуру
            )
            await state.clear()
            return
        else:
            try:
                for rows in info_user:
                    for _, value in rows.items():
                        await msg.answer(
                            f"{value}",
                            reply_markup=types.ReplyKeyboardRemove()  # убираем клавиатуру
                        )
            #вычищаем пользовательскую сессию
                await state.clear()
            except AttributeError:
                print('Пустой запрос') 
                
#ветка просмотра /select_address
@router.message(StateFilter(None), Command("select_info"))
async def select_address(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text="Напиши адрес, пример ниже",
            reply_markup=keyboards.make_row_keyboard(list.list_addr)   # #выборка из list_addr(временно)
        )
        await state.set_state(Select_Info.choosing_address)  #ожидание выбора на виртуальной клавиатуре
        
@router.message(Select_Info.choosing_address)
async def cmd_address(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        addr = msg.text.split(" ")
        street = addr[0]
        home = addr[1]
        if len(street) == 0 or len(home) == 0:
            await msg.answer(
            text=f"Что то не то с адресом :(",
            reply_markup = types.ReplyKeyboardRemove()  # убираем клавиатуру
            )
            await state.clear()
            return
        else:
            result = dtb.select_info(street, home)
            result_keys = dtb.select_info_keys(street, home)
            if result_keys is not None:
                k_entrance = result_keys.get('k_entrance')
                k_ind = result_keys.get('k_ind')
                k_stand = result_keys.get('k_stand')
            else:
                no_data = ' Нет данных '  
                k_entrance = no_data
                k_ind = no_data
                k_stand = 'ключ стандартный' 
            user = msg.from_user.full_name
            content = list.bot_log[2] + ': ул. ' + street + ', д. ' + home + ' в '
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            dtbs.insert_entr(user, content, time_str)
            if result is None:
                await msg.answer(
                    text=f"Что то не то с адресом :(",
                    reply_markup=types.ReplyKeyboardRemove()  # убираем клавиатуру
                )
                await state.clear()
                return
            else:
                try: 
                    for _, value in result.items():
                        await msg.answer(
                        text=f"{value}, \nПодьездов : {k_entrance}\nиндивидуальный ключ : {k_ind}\nстандартный ключ : {k_stand}",
                            reply_markup=types.ReplyKeyboardRemove()  # убираем клавиатуру
                        )
                
                    await state.clear()
                except AttributeError:
                    print('Пустой запрос')

#добавить запись в environment
@router.message(StateFilter(None), Command("add_envi"))
async def add_environment(msg: Message, state: FSMContext):
    if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"добавить запись в оборудование",
            reply_markup=keyboards.make_row_keyboard(["Введи данные через\nпробел|пробел"])
        )
        await state.set_state(Select_Info.add_info)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
            reply_markup=keyboards.make_row_keyboard(["Тип | Адрес | Дата | Проблема | Кто"])
        )
        return
    await state.set_state(Select_Info.add_info)
@router.message(Select_Info.add_info)
async def insert_environment(msg: Message, state: FSMContext):
    envi = msg.text.split("|")
    if len(envi) == 1:
        await msg.answer(f"Тогда выходим ;)")
        await state.clear()
        return
    equipment = envi[0]
    date = envi[1]
    address = envi[2]
    problem = envi[3]
    responsible = envi[4]
    print(len(envi))
    
    data = date.split("-")
    if len(data[0]) != 4 and len(data[1]) != 2 and len(data[2]) != 2:
        await msg.answer(f"Проверь данные, особенно формат даты ;)\n xxxx-xx-xx")
        await state.clear()
        return
    else: 
        date = data[0] + '-' + data[1] + '-' + data[2]
        dtb.add_envi(equipment, address, date, problem, responsible)
        login = msg.from_user.full_name
        user = list.rename.get(login)
        content = list.bot_log[3]
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        dtbs.insert_entr(user, content, time_str)
        result = dtb.sel_envi()
        for _, value in result.items():
            await msg.answer(f"{value}")
            await state.clear()
            
#посмотреть количество последних записей в оборудование (выбираем количество)
@router.message(StateFilter(None), Command("view_equip"))
async def view_last_environment(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"Количество записей",
            reply_markup=keyboards.make_row_keyboard(["только цифры"])
        )
        await state.set_state(Select_Info.view_eqiup)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        await state.set_state(Select_Info.view_eqiup)
        return
@router.message(Select_Info.view_eqiup)
async def select_last_environment(msg: Message, state: FSMContext):
    limit = msg.text
    if limit != '':
        user = msg.from_user.full_name
        content = list.bot_log[4] + limit + ' последние записи'
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        dtbs.insert_entr(user, content, time_str)
        result = dtb.sel_last_envi(limit)
        for rows in result:
            for _, value in rows.items():
                await msg.answer(f"{value}")
            await msg.answer(f"-----------")
        await state.clear()
    else:
        await msg.answer(f"Что-то не так :(")
        await state.clear()
        return
        
#удаление по id/select_address
@router.message(StateFilter(None), Command("del_equip"))
async def del_environment(msg: Message, state: FSMContext):
    if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"удаляемый id",
            reply_markup=keyboards.make_row_keyboard(["только цифры"])
        )
        await state.set_state(Select_Info.del_eqiup)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        return
    await state.set_state(Select_Info.del_eqiup)
@router.message(Select_Info.del_eqiup)
async def del_envi(msg: Message, state: FSMContext):
    ssid = msg.text
    login = msg.from_user.full_name
    user = msg.from_user.full_name
    content = list.bot_log[5]
    time_str = time.strftime("%Y-%m-%d %H:%M:%S")
    dtbs.insert_entr(user, content, time_str)
    result = dtb.delete_equip(ssid)
    if result is None:
        await state.clear()
        await msg.answer(f"уже в небытие ;)")
    else:
        await msg.answer(f"отправлено в небытие ;)")
        await state.clear()
        
#инфа по конкретному адресу
@router.message(StateFilter(None), Command("view_address"))
async def view_address_user(msg: Message, state: FSMContext):
    if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"Адрес абона",
            reply_markup=keyboards.make_row_keyboard(["через | "])
        )
        await state.set_state(Select_Info.view_address)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        return
    await state.set_state(Select_Info.view_address)
@router.message(Select_Info.view_address)
async def select_last_environment(msg: Message, state: FSMContext):
    if "|" not in msg.text and msg.text.count("|") != 2:
        await msg.answer(f"Что-то не то с данными :(")
        await state.clear()
        return
    else:
        address = msg.text.split("|")
        street = address[0]
        home = address[1]
        namber = address[2]
        if street != '' and home != '' and namber != '':
            result = dtb.select_address_user(street, home, namber)
            user = msg.from_user.full_name
            content = list.bot_log[5] + ' /скрыто/ '
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            dtbs.insert_entr(user, content, time_str)
            try: 
                for rows in result:
                    for _, value in rows.items():
                        await msg.answer(f"{value}")
                    await msg.answer(f"-----------")
                await state.clear()
            
            except AttributeError:
                await msg.answer(f"Что-то пошло не так :(")
                await state.clear()
                return
                
#поиск по фамилии
@router.message(StateFilter(None), Command("view_name"))
async def view_old_user(msg: Message, state: FSMContext):
    if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"Введи фамилию",
            reply_markup=keyboards.make_row_keyboard(["Сидоров"])
        )
        await state.set_state(Select_Info.view_user)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        return
    await state.set_state(Select_Info.view_user)
@router.message(Select_Info.view_user)
async def select_old_user(msg: Message, state: FSMContext):
    if msg.text == '':
        await msg.answer(f"Что-то не то с данными :(")
        await state.clear()
        return
    else:
        name = msg.text
        result = dtb.select_name_user(name)
        try: 
            user = msg.from_user.full_name
            content = list.bot_log[6] + name
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            dtbs.insert_entr(user, content, time_str)
            for rows in result:
                for _, value in rows.items():
                    await msg.answer(f"{value}")
                await msg.answer(f"-----------")
            await state.clear()
        except AttributeError:
            await msg.answer(f"Что-то пошло не так :(")
            await state.clear()
            return
            
#поиск БС по номеру
@router.message(StateFilter(None), Command("view_namber_bs"))
async def view_namber_bs(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"номер БС",
            reply_markup=keyboards.make_row_keyboard(["474"])
        )
        await state.set_state(Select_Info.view_bs)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        return
    await state.set_state(Select_Info.view_bs)
@router.message(Select_Info.view_bs)
async def select_bs(msg: Message, state: FSMContext):
    if msg.text is None:
        await msg.answer(f"Что-то не то с данными :(")
        await state.clear()
        return
    else:
        namber = msg.text
        result = dtb.select_bs(namber)
        user = msg.from_user.full_name
        content = list.bot_log[7] + namber + ' по номеру базовой в '
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        dtbs.insert_entr(user, content, time_str) 
        print(result)
        try: 
             for _, value in result.items():
                 await msg.answer(f"{value}")  
             await state.clear()                 
        except AttributeError:
            await state.clear()
        
#поиск БС по адресу(частичное совпадение)
@router.message(StateFilter(None), Command("view_address_bs"))
async def view_namber_bs(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"адрес БС",
            reply_markup=keyboards.make_row_keyboard(["Ленина"])
        )
        await state.set_state(Select_Info.view_address_bs)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        await state.clear()
        return
    await state.set_state(Select_Info.view_address_bs)
@router.message(Select_Info.view_address_bs)
async def select_bs(msg: Message, state: FSMContext):
    if msg.text is None:
        await msg.answer(f"Что-то не то с данными :(")
        await state.clear()
    else:
        address = msg.text
        result = dtb.select_address_bs(address)
        user = msg.from_user.full_name
        content = list.bot_log[7] + 'по частичному запросу ' + address + ' в '
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        dtbs.insert_entr(user, content, time_str)
        try: 
            for rows in result:
                for _, value in rows.items():
                    await msg.answer(f"{value}") 
                await state.clear()                 
        except AttributeError:
            await state.clear()
            return

#снятые АСКУЭ
@router.message(StateFilter(None), Command("del_ascue"))
async def view_del_ascue(msg: Message):
     if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
         del_ascue = dtb.select_ascue_del()  # снятые АСКУЭ
         try: 
             user = msg.from_user.full_name
             content = list.bot_log[8] 
             time_str = time.strftime("%Y-%m-%d %H:%M:%S")
             dtbs.insert_entr(user, content, time_str)  
             for rows in del_ascue:
                 for _, value in rows.items():
                     await msg.answer(f"{value}")                                   
         except AttributeError:
             print('Пустой запрос')   

# добавить запись в info
@router.message(StateFilter(None), Command("add_new_info"))
async def add_new_info(msg: Message, state: FSMContext):
    if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"добавить запись в info",
            reply_markup=keyboards.make_row_keyboard(["реестр|дата|город|улица|дом|квартира|ФИО|к1|к2|к3|кон"])
        )
        await state.set_state(Select_Info.add_new_info)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        return
    await state.set_state(Select_Info.add_new_info)

@router.message(Select_Info.add_new_info)
async def insert_new_info(msg: Message, state: FSMContext):
    #reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector
    info = msg.text.split('|')
    if len(info) == 1:
        await msg.answer(f"Тогда выходим ;)")
        await state.clear()
        return
    reestr = info[0]
    date = info[1]
    sity = info[2]
    street = info[3]
    home = info[4]
    apartment = info[5]
    name = info[6]
    cable_1 = info[7]
    cable_2 = info[8]
    cable_3 = info[9]
    connector = info[10]
    if len(info) != 11:
        await msg.answer(f"Что-то не так с данными :(")
        await state.clear()
        return
    data = date.split("-")
    if len(data[0]) != 4 and len(data[1]) != 2 and len(data[2]) != 2:
        await msg.answer(f"Проверь данные, особенно формат даты ;)\n xxxx-xx-xx")
        await state.clear()
        return
    else:
        date = data[0] + '-' + data[1] + '-' + data[2]
        dtb.add_new_info(reestr, date, sity, street, home, apartment, name, cable_1, cable_2, cable_3, connector)
        login = msg.from_user.full_name
        user = list.rename.get(login)
        content = list.bot_log[10] + 'по данным ' + name
        time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        dtbs.insert_entr(user, content, time_str)
        result = dtb.view_last_new_user()
        for _, value in result.items():
            await msg.answer(f"{value}")
            await state.clear()

#поиск АЗС по номеру
@router.message(StateFilter(None), Command("view_azs"))
async def view_namber_azs(msg: Message, state: FSMContext):
    if (msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        await msg.answer(
            text=f"номер АЗС",
            reply_markup=keyboards.make_row_keyboard(["АЗС-52"])
        )
        await state.set_state(Select_Info.view_azs)
    else:
        await msg.answer(
            text=f"недостаточно прав доступа :(",
        )
        return
    await state.set_state(Select_Info.view_azs)
@router.message(Select_Info.view_azs)
async def select_azs(msg: Message, state: FSMContext):
    if msg.text is None:
        await msg.answer(f"АЗС отсутсвует в списке :(")
        await state.clear()
        return
    else:
        namber = msg.text
        if namber != '':
            result = dtb.select_azs(namber)
            user = msg.from_user.full_name
            content = list.bot_log[9] + 'по данным ' + namber
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            dtbs.insert_entr(user, content, time_str)  
            try: 
                for _, value in result.items():
                    await msg.answer(f"{value}") 
                await state.clear()
            except AttributeError: 
                await msg.answer(text=f"Нет такой АЗС :(")
                return  

#внешние ссылки
@router.message(Command("inline_url"))
async def cmd_inline_url(msg: types.Message):
     if (msg.from_user.first_name in list.log_superadmin and msg.from_user.id in list.id_admin
            and Registred.admin_OK is True):    #проверка админа
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="График",
            url=list.list_link[0])
        )
        builder.row(types.InlineKeyboardButton(
            text="ТО",
            url=list.list_link[1])
        )
        builder.row(types.InlineKeyboardButton(
            text="Архив фото-2024",
            url=list.list_link[2])
        )
        await msg.answer(
            'Куда пойдём?',
            reply_markup=builder.as_markup(),
        )
