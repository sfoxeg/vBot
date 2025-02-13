from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(
    url='sqlite:///sqlite3.db',
    echo=False
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
