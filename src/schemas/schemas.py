from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CryptoData(BaseModel):
    crypto_id: Optional[str]
    symbol: Optional[str]
    name: Optional[str]
    image: Optional[str]
    current_price: Optional[float]
    market_cap: Optional[float]
    market_cap_rank: Optional[int]
    fully_diluted_valuation: Optional[float]
    total_volume: Optional[float]
    high_24h: Optional[float]
    low_24h: Optional[float]
    price_change_24h: Optional[float]
    price_change_percentage_1h: Optional[float]
    price_change_percentage_24h: Optional[float]
    price_change_percentage_7d: Optional[float]
    price_change_percentage_30d: Optional[float]
    price_change_percentage_1y: Optional[float]
    market_cap_change_24h: Optional[float]
    market_cap_change_percentage_24h: Optional[float]
    circulating_supply: Optional[float]
    total_supply: Optional[float]
    max_supply: Optional[float]
    ath: Optional[float]
    ath_change_percentage: Optional[float]
    atl_date: datetime
    last_updated: datetime
