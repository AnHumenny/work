import config

dtb = config.telega_SQL(host=config.host, port=config.port, user=config.user,
                        password=config.password, dtb=config.dtb)

def inputs():
    try:
        yield input().split(',')
    except (ValueError, EOFError):
        return

def insert():
    for login, name, status, password, phone, email in inputs():
        dtb.check_new_user(login, name, status, password, phone, email)
        return

insert()

