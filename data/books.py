from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class Book(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    image_data = Column(BLOB, nullable=True)