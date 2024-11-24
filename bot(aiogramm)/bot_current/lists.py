import os
from dotenv import load_dotenv

load_dotenv()

helps = [
        "/current_shedule - посмотреть курсы\n",
        "/current_image - посмотреть графику\n",
        ]

list_url = [
    "https://myfin.by/currency/torgi-na-bvfb/kurs-dollara",
    "https://myfin.by/currency/torgi-na-bvfb/kurs-euro",
    "https://myfin.by/currency/torgi-na-bvfb/kurs-rublya",
    "https://myfin.by/currency/torgi-na-bvfb/kurs-cny"
]

check_list = ["USD", "EUR", "RUB", "CNY"]
log_admin = os.getenv('log_admin')
id_user = os.getenv('id_user')
access = os.getenv('access')

