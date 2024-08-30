from shemas.database import DGazprom, DBaseStation, DAllInfo, DManual, new_session
from sqlalchemy import select, insert, text


class SearchInfo:

    #блок search
    #выборка конкретной АЗС, БС
    @classmethod
    async def select_all_search(cls, value):
        async with new_session() as session:
            value = value.split(", ")
            if value[0] == 'namber_bs':
                q = select(DBaseStation).where(DBaseStation.number == value[1])
            if value[0] == 'azs':
                q = select(DGazprom).where(DGazprom.number == value[1])
            answer = await session.scalar(q)
            await session.close()
            return answer

    #групповое по кластерам, улицам
    @classmethod
    async def select_all_claster_street(cls, value):
        async with new_session() as session:
            value = value.split(", ")
            print(value[0], value[1], value[2])
            if value[0] == 'street_fttx':
                q = select(DAllInfo).where(DAllInfo.sity == value[1], DAllInfo.street == value[2])
            if value[0] == 'claster_fttx':
                q = select(DAllInfo).where(DAllInfo.sity == value[1], DAllInfo.claster == value[2])
            answer = await session.scalars(q)
            await session.close()
            return answer

    #выборка по АЗС
    @classmethod
    async def select_gazprom(cls, value):
        async with new_session() as session:
            value = value.split(", ")
            q = select(DGazprom).where(DGazprom.number == value[1])
            answer = await session.scalar(q)
            await session.close()
            return answer


    #все кластера
    @classmethod
    async def select_claster(cls, value):
        async with new_session() as session:
            value = value.split(", ")
            q = select(DAllInfo).where(DAllInfo.sity == value[1], DAllInfo.claster == value[2])
            answer = await session.scalars(q)
            print('ответ', answer)
            await session.close()
            return answer

    # выборка по АЗС
    @classmethod
    async def select_one_fttx(cls, value):
        async with new_session() as session:
            value = value.split(", ")
            q = select(DAllInfo).where(DAllInfo.sity == value[1], DAllInfo.street == value[2], DAllInfo.namber == value[3])
            answer = await session.scalar(q)
            await session.close()
            return answer

    #end блок search
    #start блок все заправки, все базовые, мануал
    @classmethod
    async def select_azs_bs_manual(cls, value):
        async with new_session() as session:
            if value == 'azs':
                q = select(DGazprom)
            if value == 'bs':
                q = select(DBaseStation)
            if value == 'man':
                q = select(DManual)
            answer = await session.scalars(q)
            await session.close()
            return answer