from sqlalchemy import Column, Integer, String, TIMESTAMP, Float
from src.core.db import Base


class Crypto(Base):
    __tablename__ = "crypto"

    id = Column(Integer, primary_key=True)
    crypto_id = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    name = Column(String, nullable=False)
    image = Column(String)
    current_price = Column(Float)
    market_cap = Column(Float)
    market_cap_rank = Column(Integer)
    fully_diluted_valuation = Column(Float)
    total_volume = Column(Float)
    high_24h = Column(Float)
    low_24h = Column(Float)
    price_change_24h = Column(Float)
    price_change_percentage_1h = Column(Float)
    price_change_percentage_24h = Column(Float)
    price_change_percentage_7d = Column(Float)
    price_change_percentage_30d = Column(Float)
    price_change_percentage_1y = Column(Float)
    market_cap_change_24h = Column(Float)
    market_cap_change_percentage_24h = Column(Float)
    circulating_supply = Column(Float)
    total_supply = Column(Float)
    max_supply = Column(Float)
    ath = Column(Float)
    ath_change_percentage = Column(Float)
    atl_date = Column(TIMESTAMP(timezone=True))
    last_updated = Column(TIMESTAMP(timezone=True))