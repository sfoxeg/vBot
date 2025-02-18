from sqlalchemy import select
from database import session_factory
from models import UsersOrm, SearchSettingsOrm


class User:

    def __init__(self):
        self.search_age_max = None
        self.search_age_min = None
        self.search_gender = None
        self.photo = None
        self.gender = None
        self.desc = None
        self.age = None
        self.name = None
        self.chat_id = None
        self.id = None

    def get_profile(self, chat_id: str) -> None:
        self.reg(chat_id)
        with session_factory() as session:
            query = select(UsersOrm).filter_by(chat_id=chat_id)
            result = session.execute(query).scalars().first()
            usr = result

            if usr:
                self.id = usr.id
                self.chat_id = usr.chat_id
                self.name = usr.name
                self.age = usr.age
                self.desc = usr.desc
                self.gender = usr.gender
                self.photo = usr.photo
                self.search_gender = usr.search_setting.gender
                self.search_age_min = usr.search_setting.age_min
                self.search_age_max = usr.search_setting.age_max

    def update_profile(self) -> None:
        with session_factory() as session:
            usr = session.get(UsersOrm, self.id)
            usr.chat_id = self.chat_id
            usr.name = self.name
            usr.age = self.age
            usr.desc = self.desc
            usr.gender = self.gender
            usr.photo = self.photo
            session.commit()

    def update_search_setting(self) -> None:
        with session_factory() as session:
            usr = session.get(UsersOrm, self.id)
            usr.search_setting.gender = self.search_gender
            usr.search_setting.age_min = self.search_age_min
            usr.search_setting.age_max = self.search_age_max
            session.commit()

    @staticmethod
    def reg(chat_id: str) -> None:
        with session_factory() as session:
            query = select(UsersOrm.chat_id).filter_by(chat_id=chat_id)
            result = session.execute(query)
            usr = result.first()
            if usr is None:
                usr = UsersOrm(chat_id=chat_id)
                usr.search_setting = SearchSettingsOrm()
                session.add(usr)
                session.commit()


user = User()
