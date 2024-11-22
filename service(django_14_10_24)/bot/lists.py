import os
from dotenv import load_dotenv
load_dotenv()

help = ["/help - мануал по боту\n",
        "/contact - контактная информация\n",
        "/view_azs - посмотреть автозаправки Газпром\n",
        "/view_bs_id - посмотреть БС по номеру\n",
        "/view_bs_address - посмотреть БС по адресу\n",
        "/view_all_info - посмотреть данные fttx\n",
        "/view_man - посмотреть manual\n",
        "/add_new_info - добавить в info\n",
        "/update_accident - обновить инцидент по номеру\n",
        "/charts - графики\n",
        "/view_accident - посмотреть инциденты\n",
        "/view_accident_number - посмотреть инциденты номеру\n",
      #   "/view_tracks - трассы"
        ]
status = ["open", "close", "check"]

block_word = [
    "Гомель"
]


adm_help = [
           ]

contact = [
        "+375297576571 - будние с 9.00 до 17.00",
        "+375297576066 - ежедневно с 9.00 до 21.00",
        "0860 - короткий КЦ",
        "+375292503590 - Альпы смена",
        "+375292503453 - Андрей Клиндюк",
        "+375292503732 - Сергей Бугор",
        "+375297776142 - Андрей Белозёров",
        "+375336663151 - Сергей Чабак",
        "+375297370731 - Александр Власов",
        ]

log_admin = os.getenv('log_admin')
id_user = os.getenv('id_user')
access = os.getenv('access')

