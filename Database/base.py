from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///puskesmas.Database')

_SessionFactory = sessionmaker(bind=engine)

connection = engine.connect()

def sessionFactory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
