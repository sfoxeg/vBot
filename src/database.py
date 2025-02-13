from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS

'''url = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
'''
url = URL.create(drivername='postgresql+psycopg2',
                 username=DB_USER,
                 password=DB_PASS,
                 database=DB_NAME,
                 host=DB_HOST,
                 port=DB_PORT)
print(url)
engine = create_engine(url=url, echo=False)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
