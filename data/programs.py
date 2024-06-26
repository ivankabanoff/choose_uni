import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Programs(SqlAlchemyBase):
    __tablename__ = 'programs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    university_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), index=True)
    faculty = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    region = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('regions.id'), index=True)
    city = sqlalchemy.Column(sqlalchemy.String, index=True)
    link = sqlalchemy.Column(sqlalchemy.String)
    ege = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('ege.id'), index=True)
    admin = orm.relationship('User')
    reg = orm.relationship('Region')
    ege_points = orm.relationship("Ege")
