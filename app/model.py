from sqlalchemy import Column, Integer, String
from .config import Base, engine, CRUD_mixing


class Name(Base, CRUD_mixing):
    __tablename__ = "names"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))

    def __repr__(self):
        return "<Name(first_name='%s/', last_name='%s/')>" % (
            self.first_name,
            self.last_name
        )


Base.metadata.create_all(bind=engine)
