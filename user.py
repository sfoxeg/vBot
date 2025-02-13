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
        with session_factory() as session:
            query = select(UsersOrm).filter_by(chat_id=chat_id)
            result = session.execute(query).scalars().first()
            user = result

            if user:
                self.id = user.id
                self.chat_id = user.chat_id
                self.name = user.name
                self.age = user.age
                self.desc = user.desc
                self.gender = user.gender
                self.photo = user.photo

    def update_profile(self, chat_id: str):
        with session_factory() as session:
            user = session.get(UsersOrm, self.id)
            user.chat_id = self.chat_id
            user.name = self.name
            user.age = self.age
            user.desc = self.desc
            user.gender = self.gender
            user.photo = self.photo
            session.commit()


def reg_user(chat_id: str) -> None:
    with session_factory() as session:
        query = select(UsersOrm.chat_id).filter_by(chat_id=chat_id)
        result = session.execute(query)
        user = result.first()
        if user is None:
            session.add(UsersOrm(chat_id=chat_id))
            session.commit()
