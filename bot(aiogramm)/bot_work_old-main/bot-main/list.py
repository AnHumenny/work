help = [
        "лист /help part 1"   #общий, доработать
        ]
adm_help = [
            "лист /help лист /help part 2" 
           ]
available_user_names = ["пример запроса"]

log_superadmin = ["name"]     #полный доступ
id_user = ["name"]            #общий доступ, доработать
log_admin = ["name"]          #список пользователей с частичным доступом запросов к БД
id_admin = [id]               #список ID пользователей

mts = [
        "блок контактов МТС"
        ]

contact = [
        "контакты суб"
        ]
list_addr = ["пример запроса"]
list_link = [
             "блок внешних ссылок"
]
rename = {
    'rename user -> имя при внесении изменений в БД'
}

#логирование действий групп admin/superadmin(в PostGre)
bot_log = [
          'зашёл в чат в ',
          'посмотрел список сотрудников в ',
          'посмотрел данные по адресу ',
          'добавил запись в replacement в ',
          'посмотрел в replacement ',
          'посмотрел данные по адресу ',
          'посмотрел данные по фамилии ',
          'посмотрел данные БС ',
          'посмотрел  снятые АСКУЭ ',
          'посмотрел данные по ',
          'добавил данные в info по ',
]
