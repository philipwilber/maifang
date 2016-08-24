# -*- coding: utf-8 -*-
from consts import const
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tbORM

class DBORMProvider(object):
    engine = create_engine(
        'mysql+mysqlconnector://%s:%s@%s/%s?charset=utf8' % (const.DB_USER, const.DB_PASSWORD, const.DB_ADRESS,
                                                             const.DB_LIANJIA), encoding=const.ENCODE_FORM, echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ershou1 = session.query(tbORM.DB_ershou).all()
    print(type(ershou1))
    print(ershou1[0].name)






