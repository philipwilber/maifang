# -*- coding: utf-8 -*-
from consts import const

from sqlalchemy import create_engine

engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' % (const.DB_USER, const.DB_PASSWORD, const.DB_ADRESS,
                                                             const.DB_LIANJIA), encoding=const.ENCODE_FORM, echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class db_ershou(object):
    __tablename__ = const.TB_ERSHOU
