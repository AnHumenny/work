from dotenv import load_dotenv
import os
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
from aiogram import types, F, Router, Bot
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import as_list
from aiogram.utils.keyboard import InlineKeyboardBuilder
import base64
import lists
from aiogram.fsm.state import StatesGroup, State
import keyboards
from repository import Repo
from time import sleep
from create_graf import get_currency_rate

router = Router()

class SelectInfo(StatesGroup):
    register_user = State()

class Registred:
    user_OK = False
    available_user_names = []
    login = ''
    name = ''
    count = 0

@router.message(StateFilter(None), Command("start"))
async def start_handler(msg: Message, state=FSMContext):
    await msg.answer("Привет! \n")
    await msg.answer(
        text="Знаешь как зайти? :)",
        reply_markup=keyboards.make_row_keyboard(['xxxxxx'])
    )
    await state.set_state(SelectInfo.register_user)

@router.message(SelectInfo.register_user)
async def cmd_auth(msg: Message, state: FSMContext):
    if Registred.count > 3:
        Registred.count = 0
    bot = Bot(token=API_TOKEN)
    autent = msg.text.split('|')
    if len(autent) != 2:
        Registred.count += 1
        await msg.answer(
            text=f"Что то за не то с паролем :("
        )
        print("count", Registred.count)
        if Registred.count == 3:
            await msg.answer(
                text="Теперь ждём минуту :("
            )
            l = [0, msg.from_user.id, msg.date, f"{msg.from_user.id} три некорректные авторизации :)"]
            await Repo.insert_into_date(l)
            print("count", Registred.count)
            sleep(60)
        return
    else:
        Registred.count += 1
        auth = msg.text.split("|")
        login = auth[0]
        pswrd = auth[1]
        pass_wrd = pswrd.encode('utf-8')
        pwd = base64.b64encode(pass_wrd)
        if len(login) == 0 or len(pwd) < 7:
            await msg.answer(
                text=f"Что то не получилось с паролем :("
            )
            print("count", Registred.count)
            if Registred.count == 3:
                await msg.answer(
                    text="Теперь ждём минуту :("
                    )
                l = [0, msg.from_user.id, msg.date, f"{msg.from_user.id} три неверных попытки подбора пароля :)"]
                await Repo.insert_into_date(l)
                sleep(60)
            await state.clear()
            return
        else:
            result = await Repo.select_pass(login, pwd, msg.from_user.id)
            if result is None:
                await msg.answer(
                    text=f"Не зашло с паролем :("
                    )
                Registred.count += 1
                if Registred.count == 3:
                    await msg.answer(
                        text="Теперь ждём минуту :("
                        )
                    l = [0, msg.from_user.id, msg.date, f"{msg.from_user.id} три хаотичных пароля :)"]
                    await Repo.insert_into_date(l)
                    sleep(60)
                    await state.clear()
                    return
            else:
                if result.tg_id not in lists.access:
                    await msg.answer(
                        text=f"Упс. Что то не так с данными :("
                    )
                    return
                if result.tg_id in lists.access:
                    Registred.user_OK = True
                    Registred.login = result.login
                    Registred.name = result.name
                await msg.answer(
                    text=f"Набери\n/help, {result.name}"
                    )
                await bot.send_message(408397675, 'В бот зашёл ' + result.name)
                await state.clear()
                return

@router.message(F.text, Command("help"))
async def cmd_help(msg: Message):
    if Registred.login not in lists.id_user and Registred.user_OK is False:
        await msg.answer(
            text=f"Увы. Нет доступа к внутренней информации :("
        )
        return
    else:
        content = as_list(*lists.helps)
        await msg.answer(**content.as_kwargs())

@router.message(Command("current_shedule"))
async def cmd_random(message: types.Message):
    if Registred.login not in lists.id_user and Registred.user_OK is False:
        await message.answer(
            text=f"недостаточно прав доступа :("
        )
        return
    else:
        builder = InlineKeyboardBuilder()

        builder.row(types.InlineKeyboardButton(
            text="USD",
            callback_data="USD")
        )
        builder.add(types.InlineKeyboardButton(
            text="EURO",
            callback_data="EURO")
        )
        builder.row(types.InlineKeyboardButton(
            text="RUR",
            callback_data="RUR")
        )
        builder.add(types.InlineKeyboardButton(
            text="CNY",
            callback_data="CNY")
        )
        await message.answer(
            "Что надо?",
            reply_markup=builder.as_markup()
        )

@router.callback_query(F.data == "USD")
async def send_current_exchange(callback: types.CallbackQuery):
    res = get_currency_rate("USD")
    with open(f'{os.getcwd()}/media/image_USD.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'usd')
    await callback.message.answer(f"Курс доллара\n {res}")
    await callback.message.answer_photo(photo)

@router.callback_query(F.data == "EURO")
async def send_current_exchange(callback: types.CallbackQuery):
    res = get_currency_rate("EUR")
    with open(f'{os.getcwd()}/media/image_EUR.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'euro')
    await callback.message.answer(f"Курс евро\n {res}")
    await callback.message.answer_photo(photo)

@router.callback_query(F.data == "RUR")
async def send_current_exchange(callback: types.CallbackQuery):
    res = get_currency_rate("RUB")
    with open(f'{os.getcwd()}/media/image_RUB.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'rub')
    await callback.message.answer(f"Курс российского рубля\n100 росс.руб. - {res}")
    await callback.message.answer_photo(photo)

@router.callback_query(F.data == "CNY")
async def send_current_exchange(callback: types.CallbackQuery):
    res = get_currency_rate("CNY")
    with open(f'{os.getcwd()}/media/image_CNY.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'cny')
    await callback.message.answer(f"Курс юаня\n10 юаней - {res}")
    await callback.message.answer_photo(photo)

@router.message(Command("current_image"))
async def cmd_random(message: types.Message):
    if Registred.login not in lists.id_user and Registred.user_OK is False:  # проверка статуса
        await message.answer(
            text=f"недостаточно прав доступа :("
        )
        return
    else:
        builder = InlineKeyboardBuilder()

        builder.row(types.InlineKeyboardButton(
            text="Статистика USD",
            callback_data="graf_usd")
        )
        builder.add(types.InlineKeyboardButton(
            text="Статистика EURO",
            callback_data="graf_euro")
        )
        builder.row(types.InlineKeyboardButton(
            text="Статистика RUR",
            callback_data="graf_rub")
        )
        builder.add(types.InlineKeyboardButton(
            text="Статистика CNY",
            callback_data="graf_cny")
        )

        builder.row(types.InlineKeyboardButton(
            text="Стат за 5 дней ",
            callback_data="graf_all")
        )

        await message.answer(
            "Что надо?",
            reply_markup=builder.as_markup()
        )

@router.callback_query(F.data == "graf_usd")
async def send_current_graf(callback: types.CallbackQuery):
    with open(f'{os.getcwd()}/media/image_USD.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'graf_uero')
        await callback.message.answer_photo(photo)

@router.callback_query(F.data == "graf_euro")
async def send_current_graf(callback: types.CallbackQuery):
    with open(f'{os.getcwd()}/media/image_EUR.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'graf_uero')
    await callback.message.answer_photo(photo)

@router.callback_query(F.data == "graf_rub")
async def send_current_graf(callback: types.CallbackQuery):
    with open(f'{os.getcwd()}/media/image_RUB.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'graf_rub')
    await callback.message.answer_photo(photo)

@router.callback_query(F.data == "graf_cny")
async def send_current_graf(callback: types.CallbackQuery):
    with open(f'{os.getcwd()}/media/image_CNY.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'graf_cny')
    await callback.message.answer_photo(photo)

@router.callback_query(F.data == "graf_all")
async def send_current_graf(callback: types.CallbackQuery):
    with open(f'{os.getcwd()}/media/image_all.png', 'rb') as file:
        photo = BufferedInputFile(file.read(), 'image_all.png')
        await callback.message.answer_photo(photo)
