from argparse import ArgumentParser
from database import engine, Base
from models import UsersOrm

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("create", type=bool, default=False, help="Create tables")

    args = parser.parse_args()

    if args.create:
        print("Drop tables")
        Base.metadata.drop_all(engine)
        print("Create tables")
        engine.echo = True
        Base.metadata.create_all(engine)
