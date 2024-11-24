from sqlalchemy import select, insert, update
from database import (DGazprom, DManual, DBaseStation, DAllInfo, DKey, DConnFromBs,
                      new_session, DInfo, DReplacement)

class Repo:
    @classmethod
    async def select_azs_all(cls):      #выборка АЗС Газпром
        async with new_session() as session:
            q = select(DGazprom)
            result = await session.execute(q)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def select_man_all(cls):                 #мануал
        async with new_session() as session:
            q = select(DManual)
            result = await session.execute(q)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def select_ascue_all(cls):                #АСКУЭ
        async with new_session() as session:
            q = select(DAllInfo)
            result = await session.execute(q)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def select_conn_from_base(cls):         #индивидуальные трассы
        async with new_session() as session:
            q = select(DConnFromBs)
            result = await session.execute(q)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def select_keys_all(cls):                #ключи от шкафов с оборудованием
        async with new_session() as session:
            q = select(DKey)
            result = await session.execute(q)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def search_bs_number(cls, number):      #базовые по номерам
        async with new_session() as session:
            query = select(DBaseStation).where(DBaseStation.number == int(number))
            result = await session.execute(query)
            answer = result.scalar()
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def search_bs_address(cls, address):    #базовая по частичному совпадению
        async with new_session() as session:
            query = select(DBaseStation).where(DBaseStation.address.like(f"%{address}%"))
            result = await session.execute(query)
            answer = result.scalars().all()
            for row in result:
                print(row.address)
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def select_all_info(cls, temp):
        async with new_session() as session:
            result = temp.split(", ")
            query = select(DAllInfo).where(DAllInfo.sity == result[0], DAllInfo.street == result[1], DAllInfo.namber == result[2])
            result = await session.execute(query)
            answer = result.scalar()
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def select_claster(cls, claster):    #выборка по кластеру
        async with new_session() as session:
            query = select(DAllInfo).where(DAllInfo.claster == claster)
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def select_street(cls, street):    #выборка по улице
        async with new_session() as session:
            query = select(DAllInfo).where(DAllInfo.street == street)
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.commit()
            await session.close()
            return answer

    @classmethod      #доработать!
    async def update_info_fttx(cls, ssid, value):  #обновление комментария в основной таблице
        async with new_session() as session:
            q = update(DAllInfo).where(DAllInfo.id == ssid).values(comment=value)
            await session.execute(q)
            await session.commit()
            await session.close()
            return

    @classmethod
    async def insert_user_info(cls, l):  #добавить в реестры
        async with new_session() as session:
            q = insert(DInfo).values(l)
            await session.execute(q)
            await session.commit()
            await session.close()
            return

    @classmethod
    async def select_users(cls):     #выборка в Инфо последние 20 абонов
        async with new_session() as session:
            query = select(DInfo).order_by(DInfo.id.desc()).limit(20)
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def select_replacement(cls):  # выборка в replacement последние 10 записей
        async with new_session() as session:
            query = select(DReplacement).order_by(DReplacement.id.desc()).limit(20)
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def insert_into_replacement(cls, l):  # добавить в реестры
        async with new_session() as session:
            q = insert(DReplacement).values(l)
            await session.execute(q)
            await session.commit()
            await session.close()
            return

    @classmethod
    async def csv_export_fttx(cls):  # export replacement
        async with new_session() as session:
            query = select(DReplacement).order_by(DReplacement.id.desc())
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def csv_export_fttx_users(cls, date_1, date_2):  # export абонов выборка по дате
        async with new_session() as session:
            query = select(DInfo).where(DInfo.date.between(date_1, date_2)).order_by(DInfo.id.asc())
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.close()
            return answer
