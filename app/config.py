from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///database.db", echo=False)


Session = sessionmaker(bind=engine)
session = Session()


class CRUD_mixing:
    def save(self):
        session.add(self)
        session.commit()
        return self

    def delete(self):
        session.delete(self)
        session.commit()
        return
