from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
import func
import csv
import base64
import random

dtb = func.AuthMysql(host=func.host, port=func.port, user=func.user,
                     password=func.password, dtb=func.dtb)
SESSION_TYPE = 'memcache'
app = Flask(__name__)
app.secret_key = "super secret key"

class Registred:
    admin_OK = False
    marketing_OK = False

#основная страница + графика по текущему году
@app.route('/')
def index():
    date_0_0 = '2021-01-01'
    date_0_1 = '2021-12-31'
    date_1 = '2022-01-01'
    date_2 = '2022-12-31'
    date_3 = '2023-01-01'
    date_4 = '2023-12-31'
    date_5 = '2024-01-01'
    date_6 = '2024-12-31'
    labels = [
        'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
        'Декабрь',
    ]
    data = []
    result = dtb.select_by_year_2024()
    for rows in result:
        for _, value in rows.items():
            data.append(value)
    # Return the components to the HTML template
    return render_template(
        template_name_or_list='hello.html',
        data=data,
        labels=labels,
        greeting_0=dtb.select_year(date_0_0, date_0_1),
        greeting_1=dtb.select_year(date_1, date_2),
        greeting_2=dtb.select_year(date_3, date_4),
        greeting_3=dtb.select_year(date_5, date_6)
      #  greet=dtb.index()
    )
#мануал
@app.route('/manual/')
def manual():
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        return render_template("manual.html", select=dtb.select_manual())

#заправки газпром вся инфа
@app.route('/gazprom/')
def gazprom():
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        return render_template("gazprom.html", select=dtb.select_gazprom())

#БС вся инфа
@app.route('/base_station/')
def base_station():
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        return render_template("base_station.html", select=dtb.select_bs())

#трассы fttx
@app.route('/trassa_fttx/')
def trassa_fttx_gomel():
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        return render_template("trassa_fttx_gomel.html")

#поиск через тэг
@app.route('/search_result/', methods=['POST'])
def search_result():
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        data = request.form  # data is dictionary with form data
        list_variables = ['detail_fttx', 'street_fttx', 'namber_bs', 'claster_fttx', 'azs']
        for _, val in data.items():
            spl = val.split(', ')
            variable = spl[0].strip()
            if variable not in list_variables:
               return render_template('search_error.html')
            else:
                for _, value in data.items():
                    if variable == 'detail_fttx':
                        return render_template('search_result.html',
                                               select=dtb.select_info_detail_fttx(value),
                                               keys=dtb.select_keys(value))
                    if variable == 'street_fttx':
                        return render_template('search_result_all.html',
                                               select=dtb.select_info_detail_fttx_only_street(value))
                    if variable == 'namber_bs':
                        return render_template('search_result.html',
                                               select=dtb.select_namber_bs(value))
                    if variable == 'claster_fttx':
                        return render_template('search_result_all.html',
                                               select=dtb.select_claster_fttx(value))
                    if variable == 'azs':
                        return render_template('search_result.html',
                                               select=dtb.select_azs(value),
                                               )
#линейный плот по годам
@app.route('/grafik_linear/')
def graf_linear():
    if Registred.admin_OK is True or Registred.marketing_OK is True:
        date_0_0 = '2021-01-01'
        date_0_1 = '2021-12-31'
        date_1 = '2022-01-01'
        date_2 = '2022-12-31'
        date_3 = '2023-01-01'
        date_4 = '2023-12-31'
        date_5 = '2024-01-01'
        date_6 = '2024-12-31'
        labels = [
            'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
            'Декабрь'
        ]
        data_0 = []
        data_1 = []
        data_2 = []
        data_3 = []
        result_0 = dtb.select_by_year_2021()
        for rows in result_0:
            for _, value in rows.items():
                data_0.append(value)
        result_1 = dtb.select_by_year_2022()
        for rows in result_1:
            for _, value in rows.items():
                data_1.append(value)
        result_2 = dtb.select_by_year_2023()
        for rows in result_2:
            for _, value in rows.items():
                data_2.append(value)
        result_3 = dtb.select_by_year_2024()
        for rows in result_3:
            for _, value in rows.items():
                data_3.append(value)
        return render_template(
            template_name_or_list='grafik_linear.html',
            labels=labels,
            data_0=data_0,
            data_1=data_1,
            data_2=data_2,
            data_3=data_3,
            greeting_0=dtb.select_year(date_0_0, date_0_1),
            greeting_1=dtb.select_year(date_1, date_2),
            greeting_2=dtb.select_year(date_3, date_4),
            greeting_3=dtb.select_year(date_5, date_6)
        )
    else:
        return render_template(
            template_name_or_list='login_adm.html',
            access='Недостаточно прав доступа к этой странице'
            )

#графика по годам круг
@app.route('/grafik_pie/')
def graf_pie():
    if Registred.admin_OK is True or Registred.marketing_OK is True:
        labels = ['2021', '2022', '2023', '2024']
        data = []
        data_0 = []
        data_1 = []
        data_2 = []
        data_3 = []
        result_0 = dtb.select_by_year_2021()
        for rows in result_0:
            for _, value in rows.items():
                data_0.append(value)
        result_1 = dtb.select_by_year_2022()
        for rows in result_1:
            for _, value in rows.items():
                data_1.append(value)
        result_2 = dtb.select_by_year_2023()
        for rows in result_2:
            for _, value in rows.items():
                data_2.append(value)
        result_3 = dtb.select_by_year_2024()
        for rows in result_3:
            for _, value in rows.items():
                data_3.append(value)
        data.append(sum(data_0))
        data.append(sum(data_1))
        data.append(sum(data_2))
        data.append(sum(data_3))
        # Return the components to the HTML template
        return render_template(
            template_name_or_list='grafik_pie.html',
            labels=labels,
            data=data
        )
    else:
        return render_template(
            template_name_or_list='login_adm.html',
            access='Недостаточно прав доступа к этой странице'
        )
#блок авторизация\деавторизация
@app.route('/adm_login/', methods=['GET', 'POST'])
def admin_login():
    if 'user_id' in session:
        return render_template("admin_panel.html")
    error = None  # обнуляем переменную ошибок
    if request.method == 'POST':
        login = request.form['username']  # обрабатываем запрос с нашей формы который имеет атрибут name="username"
        password = request.form['password']  # обрабатываем запрос с нашей формы который имеет атрибут name="password"
        pass_wrd = password.encode('utf-8')
        password = base64.b64encode(pass_wrd)
        result = dtb.select_user(login, password)
        print(result)
        if result is not None:
            status = result.get('status')
            print(status)
        # теперь проверяем если данные сходятся формы с данными БД
            if status == 'admin':
                # в случае успеха создаем сессию в которую записываем id пользователя
                session['user_id'] = request.form['username']
                Registred.admin_OK = True
                # и делаем переадресацию АДМИНА на новую страницу -> в нашу адимнку
                return redirect(url_for('admin_panel'))
            if status == 'user':
                # в случае успеха создаем сессию в которую записываем id пользователя
                session['user_id'] = request.form['username']
                # и делаем переадресацию ПОЛЬЗОВАТЕЛЯ на новую страницу -> в нашу адимнку
                return redirect(url_for('admin_panel'))
            if status == 'marketing':
                # в случае успеха создаем сессию в которую записываем id пользователя
                session['user_id'] = request.form['username']
                Registred.marketing_OK = True
                # и делаем переадресацию MARKETING на новую страницу -> в нашу адимнку
                return redirect(url_for('admin_panel'))
        else:
            error = 'Неверное имя пользователя или пароль'
    return render_template('login_adm.html', error=error)
#переадресация авторизованного пользователя
@app.route('/admin_panel')
def admin_panel():
    # делаем доп проверку если сессия авторизации была создана
    if 'user_id' not in session:
        return render_template("404.html")
    if Registred.admin_OK is False:
        return render_template('login_adm.html')
    else:
        return render_template('admin_panel.html')
#выход
@app.route('/logout')
def logout():
    # Удаление данных пользователя из сессии
    session.clear()
    Registred.admin_OK = False
    Registred.marketing_OK = False
    # Перенаправление на главную страницу или страницу входа
    return redirect(url_for('admin_panel'))
#endblock

#Блок добавления\редактирования информации по абонентам
#добавить новую запись в info
@app.route('/add_fttx/')
def add_fttx():
    if 'user_id' not in session:
        return render_template("404.html")
    if Registred.admin_OK is False:
        user = f'Недостаточно прав доступа'
        return render_template("404.html", user=user)
    else:
        result = dtb.select_old_user()
        return render_template("add_fttx.html", old=result)

#страница редактирования info
@app.route('/edit_fttx/', methods=['POST', 'GET'])
def edit_fttx():
    ssid = request.form['docssid']
    if 'user_id' not in session:
        return render_template("404.html")
    if Registred.admin_OK is False:
        user = f'Недостаточно прав доступа'
        return render_template("404.html", user=user)
    else:
        result = dtb.select_ssid_user(ssid)
        ssid = request.form['docssid']
        reestr = result.get('reestr')
        data = result.get('date')
        city = result.get('sity')
        street = result.get('street')
        home = result.get('home')
        apartment = result.get('apartment')
        name = result.get('name')
        cable_1 = result.get('cable_1')
        cable_2 = result.get('cable_2')
        cable_3 = result.get('cable_3')
        connector = result.get('connector')
        result_old = dtb.select_old_user()
        if result is False:
            return render_template("add_fttx.html", res_none='некорректный  ID', old=result_old)
        else:
            return render_template("edit_fttx.html", ssid_result=result, old=result_old, reestr=reestr,
                                   data=data, city=city, street=street, home=home, apartment=apartment, name=name,
                                   cable_1=cable_1, cable_2=cable_2, cable_3=cable_3, connector=connector, ssid=ssid)
                                   
#непосредственно update
@app.route('/edit_fttx_info/', methods=['POST', 'GET'])
def edit_fttx_info():
    ssid = request.form['docssid']
    reestr = request.form['docreestr']
    data = request.form['docdata']
    city = request.form['doccity']
    street = request.form['docstreet']
    home = request.form['dochome']
    apartment = request.form['docapartment']
    name = request.form['docname']
    cable_1 = request.form['doccable_1']
    cable_2 = request.form['doccable_3']
    cable_3 = request.form['doccable_3']
    connector = request.form['docconnector']
    dtb.update_info(ssid, reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector)
    result = dtb.select_old_user()
    return render_template('add_fttx.html', old=result)

@app.route('/add_fttx_info/', methods=['POST'])
def add_fttx_info():
    reestr = request.form['docreestr']
    data = request.form['docdata']
    city = request.form['doccity']
    street = request.form['docstreet']
    home = request.form['dochome']
    apartment = request.form['docapartment']
    name = request.form['docname']
    cable_1 = request.form['doccable_1']
    cable_2 = request.form['doccable_3']
    cable_3 = request.form['doccable_3']
    connector = request.form['docconnector']
    lenght_l = [reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector]
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        if '' in lenght_l:
            return render_template('add_fttx.html', err='НЕКОРРЕКТНЫЕ ДАННЫЕ!')
        else:
            dtb.insert_new_fttx(reestr, data, city, street, home, apartment, name, cable_1, cable_2, cable_3, connector)
            result = dtb.select_old_user()
            return render_template('add_fttx.html', old=result)
#endblock

#Блок добавить\редактировать Оборудование
@app.route('/add_replacement/')
def add_replacement():
    if 'user_id' not in session:
        return render_template("404.html")
    if Registred.admin_OK is False:
        user = f'Недостаточно прав доступа'
    else:
        result = dtb.select_old_replacement()
    return render_template("add_replacement.html", old=result)

@app.route('/add_replacement_info/', methods=['POST'])
def add_replacement_info():
    tip = request.form['doctip']
    data = request.form['docdata']
    address = request.form['docaddress']
    problem = request.form['docproblem']
    equip = request.form['docrep']
    l = [tip, data, address, problem, equip]
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        if '' in l:
            return render_template('add_replacement.html', err='НЕКОРРЕКТНЫЕ ДАННЫЕ!')
        else:
            dtb.insert_new_replacement(tip, data, address, problem, equip)
            result = dtb.select_old_replacement()
            return render_template('add_replacement.html', old=result)

#страница редактирования info
@app.route('/edit_replacement/', methods=['POST', 'GET'])
def edit_replacement():
    ssid = request.form['docssid']
    print(ssid)
    if 'user_id' not in session:
        return render_template("404.html")
    else:
        result = dtb.select_ssid_replacement(ssid)
        ssid = request.form['docssid']
        data = result.get('date')
        address = result.get('address')
        equipment = result.get('equipment')
        problem = result.get('problem')
        responsible = result.get('responsible')
        print(result)
        if result is False:
            return render_template("add_replacement.html", res_none='некорректный  ID', old=result)
        else:
            return render_template("edit_replacement.html", ssid_result=result, data=data,
                                   address=address, equipment=equipment, problem=problem, responsible=responsible, ssid=ssid)

#непосредственно update
@app.route('/update_replacement/', methods=['POST', 'GET'])
def update_replacement():
    ssid = request.form['docssid']
    equipment = request.form['doctip']
    data = request.form['docdata']
    address = request.form['docaddress']
    problem = request.form['docproblem']
    responsible = request.form['docrep']
    all = [data, address, equipment,  problem, responsible]
    dtb.update_replacement(ssid, all)
    result = dtb.select_old_replacement()
    return render_template('add_replacement.html', old=result)
#endblock

#вывод csv
@app.route('/exit_csv_fttx/', methods=['POST'])
def exit_csv_fttx():
    city = request.form['doccsvcity']
    data_start = request.form['docdatacsvstart']
    data_finish = request.form['doccsvfinish']
    cursor = func.conn.cursor()
    query_support = "SELECT * FROM info WHERE sity = %s AND date BETWEEN %s AND %s"
    cursor.execute(query_support, (city, data_start, data_finish))
    result = cursor.fetchall()
    with open(f'Отчёт--{city}--{data_start}--{data_finish}.csv', 'w', newline="", encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL, lineterminator="\r")
        for row in result:
            csv_writer.writerow(row)
    report = f'Отчёт по {city} c {data_start} по {data_finish} готов'
    result = dtb.select_old_user()
    return render_template('add_fttx.html', old=result, report=report)

#новый пользователь
@app.route('/add_user/')
def add_user():
    print(session)
    print(Registred.admin_OK)
    if Registred.admin_OK is False:
        user = f'Недостаточно прав доступа'
        return render_template('add_user.html', user=user)
    else:
        result = dtb.select_auth_user()
        generate_pass = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()_-=+{}[]'
        gen_pass = ''.join(random.sample(generate_pass, 15))
        return render_template('add_user.html', auth_user=result, gen_pass=gen_pass)

#новый пользователь
@app.route('/add_new_user/', methods=['POST'])
def add_new_user():
    if 'user_id' not in session:
        return render_template("404.html")
    if Registred.admin_OK is False:
        user = f'Недостаточно прав доступа'
        return render_template('add_fttx.html', user=user)
    if Registred.admin_OK is True:
        name = request.form['docname']
        status = request.form['docstatus']
        password = request.form['docpassword']
        pass_word = password.encode('utf-8')
        password = base64.b64encode(pass_word)
        query = dtb.select_reg_user(name)
        result = dtb.create_new_user(name, status, password)
        if result is True:
            user = f'Пользователь {name} успешно добавлен!'
            return render_template('add_user.html', user=user)
        if result is False:
            user = f'Что то не так с пользователем ;('
            return render_template('add_user.html', user=user)

if __name__ == '__main__':
    COOKIE_SECURE = 'Secure'
    COOKIE_DURATION = timedelta(minutes=5)
    app.run(debug=False)
