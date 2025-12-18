# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) –
# sposób odwzorowania obiektowej architektury systemu informatycznego
# na bazę danych (lub inny element systemu) o relacyjnym charakterze.

# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///moja_baza.db')
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"{self.name}"


Base.metadata.create_all(engine)
