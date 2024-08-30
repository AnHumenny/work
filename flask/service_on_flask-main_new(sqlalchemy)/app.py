from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
import func
import csv
import base64
import random
import asyncio
from repository import SearchInfo

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
async def index():
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

@app.route('/gazprom/')
async def azs():
    value = 'azs'
    answer = await SearchInfo.select_azs_bs_manual(value)
    print('Тип', answer)
    return render_template("search/manual.html",
                           title='Все АЗС Газпром',
                           azs=answer
                           )

@app.route('/base_station/')
async def bs():
    value = 'bs'
    answer = await SearchInfo.select_azs_bs_manual(value)
    return render_template("search/manual.html",
                           title='Все базовые станции',
                           bs=answer
                           )

@app.route('/manual/')
async def manual():
    value = 'man'
    answer = await SearchInfo.select_azs_bs_manual(value)
    return render_template("search/manual.html",
                           title='Мануал',
                           man=answer
                           )

#поиск через тэг
@app.route('/search_result/', methods=['POST'])
async def search_result():
    data = request.form  # data is dictionary with form data
    list_variables = ['detail_fttx', 'street_fttx', 'namber_bs', 'claster_fttx', 'azs']
    for _, val in data.items():
        spl = val.split(', ')
        variable = spl[0].strip()
        if variable not in list_variables:
            return render_template('search/search_error.html')
        else:
            for _, value in data.items():
                if variable == 'detail_fttx':
                    answer = await SearchInfo.select_one_fttx(value)
                    if answer is None:
                        return render_template("404.html")
                    print('answer', answer.comment)
                    return render_template('search/search_one_fttx.html',
                                           title=f'данные по {answer.sity}, {answer.street}, {answer.namber} ',
                                           detail_fttx=answer
                                           )                       
                if variable == 'street_fttx':
                    temp = value.split(', ')
                    answer = await SearchInfo.select_all_claster_street(value)
                    if answer is None:
                        return render_template("404.html")
                    return render_template('search/manual.html',
                                           title=f'Групповое инфо по {temp[2]} ',
                                           street_fttx=answer)     

                if variable == 'claster_fttx':
                    claster = value.split(", ")
                    answer = await SearchInfo.select_all_claster_street(value)
                    if answer is None:
                        return render_template("404.html")
                    print('claster', answer)
                    return render_template('search/manual.html',
                                             title=f'Групповое инфо по кластерам, {claster[1]} {claster[2]}',
                                             claster=answer)      

                if variable == 'namber_bs':
                    answer = await SearchInfo.select_all_search(value)
                    if answer is None:
                        return render_template("404.html")
                    print('answer', answer.comment)
                    return render_template('search/search_one_bs.html',
                                            title=f'данные по БС - {answer.number}',
                                            namber_bs=answer
                                            )     #сделано
                if variable == 'azs':
                    azs = value.split(", ")
                    answer = await SearchInfo.select_all_search(value)
                    if answer is None:
                        return render_template("404.html")
                    return render_template('search/search_azs_one.html',
                                            title=f'данные по {azs[1]}',
                                            azs=answer
                                            )

@app.route('/trassa/')
async def fttx_gomel():
    return render_template("trassa/fttx_gomel.html")


if __name__ == '__main__':
   # COOKIE_SECURE = 'Secure'
   # COOKIE_DURATION = timedelta(minutes=5)
    app.run(debug=True)
