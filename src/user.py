from sqlalchemy import select
from database import session_factory
from models import UsersOrm


class User:

    def __init__(self):
        self.photo = None
        self.gender = None
        self.desc = None
        self.age = None
        self.name = None
        self.chat_id = None
        self.id = None

    def get_profile(self, chat_id: str):
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

    def update_profile(self):
        with session_factory() as session:
            usr = session.get(UsersOrm, self.id)
            usr.chat_id = self.chat_id
            usr.name = self.name
            usr.age = self.age
            usr.desc = self.desc
            usr.gender = self.gender
            usr.photo = self.photo
            session.commit()

    @staticmethod
    def reg(chat_id: str) -> None:
        with session_factory() as session:
            query = select(UsersOrm.chat_id).filter_by(chat_id=chat_id)
            result = session.execute(query)
            usr = result.first()
            if usr is None:
                session.add(UsersOrm(chat_id=chat_id))
                session.commit()


user = User()
