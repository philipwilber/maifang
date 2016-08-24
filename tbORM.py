from consts import const
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, DateTime, Float

class DB_deal(Base):
    __tablename__ = const.TB_DEAL
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    date = Column(DateTime, default=None)
    total_price = Column(Integer, default=-1)
    unit_price = Column(Integer, default=-1)
    url = Column(String(100))
    bedroom = Column(Integer, default=-1)
    livingroom = Column(Integer, default=-1)
    area = Column(Float, default=-1)
    toward = Column(String(20))
    fitment = Column(String(20))
    floor = Column(String(20))
    deal_date = Column(DateTime, default=None)

class DB_ershou(Base):
    __tablename__ = const.TB_ERSHOU

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(50))
    date = Column(DateTime, default=None)
    total_price = Column(Integer, default=-1)
    unit_price = Column(Integer, default=-1)
    url = Column(String(100))
    bedroom = Column(Integer, default=-1)
    livingroom = Column(Integer, default=-1)
    area = Column(Float, default=-1)
    toward = Column(String(20))
    fitment = Column(String(20))
    follows = Column(Integer, default=-1)
    visit_times = Column(Integer, default=-1)
    pub_date = Column(String(30))
    remarks = Column(String(500))