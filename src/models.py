import datetime
from typing import Annotated
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow)]


class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    chat_id: Mapped[str]
    gender: Mapped[bool | None]
    name: Mapped[str | None]
    age: Mapped[int | None]
    desc: Mapped[str | None]
    photo: Mapped[str | None]
    # created_at: Mapped[created_at]
    # updated_at: Mapped[updated_at]
