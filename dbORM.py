import sqlalchemy

from sqlalchemy import create_engine

engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8')
print(sqlalchemy.__version__)