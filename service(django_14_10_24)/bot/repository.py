from datetime import datetime
from sqlalchemy import select, insert, update
from database import (DGazprom, DManual, DUser, DVisitedUser, DBaseStation,
                                DAllInfo, DAccident, DAddInfo, new_session)


class Repo:
    @classmethod
    async def select_pass(cls, login, psw, tg_id):
        print(psw,"\n")
        async with new_session() as session:
            tg_id = str(tg_id)
            pswrd = psw.decode("UTF-8")
            password = str(pswrd)
            q = select(DUser).where(DUser.login == login, DUser.password == password,
                                    DUser.tg_id == tg_id)
            result = await session.execute(q)
            print(password)
            answer = result.scalar()
            await session.close()
            return answer


    @classmethod
    async def select_accident(cls, status):
        async with new_session() as session:
            if status == "open" or status == "check":
                q = select(DAccident).where(DAccident.status == status)
            else:
                q = select(DAccident).where(DAccident.status == status).limit(5)
            result = await session.execute(q)
            answer = result.scalars()
            await session.commit()
            await session.close()
            return answer


    @classmethod
    async def select_accident_number(cls, number):
        async with new_session() as session:
            number = str(number)
            query = select(DAccident).where(DAccident.number == number)
            result = await session.execute(query)
            answer = result.scalar()
            await session.commit()
            await session.close()
            return answer


    @classmethod
    async def select_azs(cls, number):
        async with new_session() as session:
            number = str(number)
            q = select(DGazprom).where(DGazprom.number == number)
            result = await session.execute(q)
            answer = result.scalar()
            await session.close()
            return answer

    @classmethod
    async def select_manual(cls, ssid):
        async with new_session() as session:
            q = select(DManual).where(DManual.id == int(ssid))
            result = await session.execute(q)
            answer = result.scalar()
            await session.close()
            return answer

    # # insert into _visited_users
    @classmethod
    async def insert_into_visited_date(cls, login, action):
        async with new_session() as session:
            date_created = datetime.now()
            q = DVisitedUser(login=login, date_created=date_created, action=action)
            session.add(q)
            await session.commit()
            await session.close()
            return
    #
    @classmethod
    async def select_action(cls, number):
        async with new_session() as session:
            query = select(DVisitedUser).order_by(DVisitedUser.id.desc()).limit(int(number))
            result = await session.execute(query)
            answer = result.scalars().all()
            return answer
    #
    #
    @classmethod
    async def select_bs_number(cls, number):
        async with new_session() as session:
            query = select(DBaseStation).where(DBaseStation.number == int(number))
            result = await session.execute(query)
            answer = result.scalar()
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def select_bs_address(cls, address):
        async with new_session() as session:
            print(address)
            query = select(DBaseStation).where(DBaseStation.address.like(f"%{address}%"))
            result = await session.execute(query)
            answer = result.scalars()
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def select_all_info(cls, temp):
        async with new_session() as session:
            result = temp.split(", ")
            city = str(result[0])
            street = str(result[1])
            number = str(result[2])
            query = select(DAllInfo).where(DAllInfo.city == city,
                                           DAllInfo.street == street,
                                           DAllInfo.number == number)
            result = await session.execute(query)
            answer = result.scalar()
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def select_stat(cls):
        async with new_session() as session:
            q = select(DVisitedUser).order_by(DVisitedUser.id.desc()).limit(10)
            result = await session.execute(q)
            answer = result.scalars().all()
            await session.close()
            return answer

    @classmethod
    async def insert_info(cls, info):
        async with new_session() as session:
            reestr = int(info[0])
            date = datetime.now()
            city = info[1]
            street = info[2]
            home = info[3]
            apartment = info[4]
            name = info[5]
            cable_1 = int(info[6])
            cable_2 = int(info[7])
            cable_3 = int(info[8])
            connector = int(info[9])
            # query = sqlalchemy.update(DProject).values(info) #почти рабочий вариант)) # хз как вставить актуальную дату вторым параметром в info :(
            query = await session.execute(insert(DAddInfo).values(reestr=reestr, date_created=date, city=city,
                                                                  street=street, home=home, apartment=apartment,
                                                                  name=name, cable_1=cable_1, cable_2=cable_2,
                                                                  cable_3=cable_3, connector=connector
                                                                  ))
            await session.commit()
            await session.close()
            return query

    @classmethod
    async def update_accident(cls, l):
        async with new_session() as session:
            number = str(l[0])
            decide = str(l[2])
            status = str(l[1])
            print(l)
            q = (
                update(DAccident).where(DAccident.number == number).values(decide=decide, status=status)  # .select.last_insert_id(DProject)
            )
            answer = await session.execute(q)
            await session.commit()
            await session.close()
            return answer

    @classmethod
    async def grafik_ring(cls, start_date, end_date):
        async with new_session() as session:
            query = select(DAddInfo).where(
                DAddInfo.date_created.between(start_date, end_date)
            )
            result = await session.execute(query)
            answer = result.scalars().all()
            await session.commit()
            return answer
