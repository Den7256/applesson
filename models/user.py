from backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user', cascade='save-update, merge, delete')

print(CreateTable(User.__table__))
table = CreateTable(User.__table__)