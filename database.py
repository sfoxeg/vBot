from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

url='sqlite:///sqlite3.db'

engine = create_engine(url=url, echo=False)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
