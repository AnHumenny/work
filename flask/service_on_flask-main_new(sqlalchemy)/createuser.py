import func
import base64

dtb = func.AuthMysql(host=func.host, port=func.port, user=func.user, password=func.password,
                     dtb=func.dtb)

def create_user(username,status, password):
    pass_word = password.encode('utf-8')
    password = base64.b64encode(pass_word)
    result = dtb.create_new_user(username, status, password)
    print(result)

create_user(input('Логин: '), input('status: '), input('Пароль: '))


