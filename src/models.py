from datetime import datetime
from typing import Annotated
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.utcnow)]


class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    chat_id: Mapped[str]
    gender: Mapped[bool | None]
    name: Mapped[str | None]
    age: Mapped[int | None]
    desc: Mapped[str | None]
    photo: Mapped[str | None]
    search_setting: Mapped["SearchSettingsOrm"] = relationship(back_populates="user", uselist=False, lazy="selectin")
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class SearchSettingsOrm(Base):
    __tablename__ = "search_settings"
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UsersOrm"] = relationship(back_populates="search_setting", uselist=False)
    gender: Mapped[bool | None]
    age_min: Mapped[int] = mapped_column(server_default=text("18"))
    age_max: Mapped[int]= mapped_column(server_default=text("100"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
