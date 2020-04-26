from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqllite:///puskesmas.db', echo=True)

_SessionFactory = sessionmaker(bind=engine)

def sessionFactory():
    Base.metadata.create_all(engine)
    return _SessionFactory()