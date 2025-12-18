from typing import List

import requests
from pydantic import BaseModel
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)

response_data = response.json()
print(response_data)


# {'table': 'A',
# 'currency': 'dolar amerykański',
# 'code': 'USD',
# 'rates': [{'no': '245/A/NBP/2025', 'effectiveDate': '2025-12-18', 'mid': 3.5893}]}

class Rates(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rates]


data = Currency(**response.json())
print(data)
print(data.rates[0].mid)  # 3.5893

engine = create_engine('sqlite:///currencies.db', echo=True)
Base = declarative_base()


class RatesDB(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    no = Column(String)
    effectiveDate = Column(String)
    mid = Column(Float)

    # for i in data.rates:
    #     print(i)


rate = data.rates[0]
usd = RatesDB(
    no=rate.no,
    effectiveDate=rate.effectiveDate,
    mid=rate.mid
)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(usd)
session.commit()
