import time
from lists import check_list
from create_graf import insert_exchange, create_all_graf, actual_img

if __name__ == "__main__":
    while True:
        insert_exchange()
        for row in check_list:
            actual_img(row)
        create_all_graf()
        print('ждём сутки')
        time.sleep(86400)