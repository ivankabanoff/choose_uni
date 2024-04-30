import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Ege(SqlAlchemyBase):
    __tablename__ = 'ege'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)
    russian = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    math_basic = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    math_advanced = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    physics = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    chemistry = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    history = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    social_science = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    informatics = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    biology = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    geography = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    english = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    german = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    french = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    spanish = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    chinese = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    literature = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    programme = orm.relationship('Programs', back_populates='ege_points')
