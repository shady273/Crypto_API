from datetime import datetime, timezone
from pycoingecko import CoinGeckoAPI
import logging
from src.utils.repository import AbstractRepository


def convert_to_crypto_data(data_list):
    crypto_data_list = []
    for data in data_list:
        crypto_data = {
            "crypto_id": data['id'],
            "symbol": data['symbol'],
            "name": data['name'],
            "image": data['image'],
            "current_price": data['current_price'],
            "market_cap": data['market_cap'],
            "market_cap_rank": data['market_cap_rank'],
            "fully_diluted_valuation": data['fully_diluted_valuation'],
            "total_volume": data['total_volume'],
            "high_24h": data['high_24h'],
            "low_24h": data['low_24h'],
            "price_change_24h": data['price_change_24h'],
            "price_change_percentage_1h": data['price_change_percentage_1h_in_currency'],
            "price_change_percentage_24h": data['price_change_percentage_24h'],
            "price_change_percentage_7d": data['price_change_percentage_7d_in_currency'],
            "price_change_percentage_30d": data['price_change_percentage_30d_in_currency'],
            "price_change_percentage_1y": data['price_change_percentage_1y_in_currency'],
            "market_cap_change_24h": data['market_cap_change_24h'],
            "market_cap_change_percentage_24h": data['market_cap_change_percentage_24h'],
            "circulating_supply": data['circulating_supply'],
            "total_supply": data['total_supply'],
            "max_supply": data['max_supply'],
            "ath": data['ath'],
            "ath_change_percentage": data['ath_change_percentage'],
            "atl_date": datetime.fromisoformat(data['atl_date']).replace(tzinfo=timezone.utc),
            "last_updated": datetime.fromisoformat(data['last_updated']).replace(tzinfo=timezone.utc)
        }
        crypto_data_list.append(crypto_data)
    return crypto_data_list


class CryptoServices:
    def __init__(self, crypto_repo: AbstractRepository):
        self.crypto_repo = crypto_repo
        self.cg = CoinGeckoAPI()
        self.logger = logging.getLogger("root")

    async def update_crypto(self):
        self.logger.info(f"Crypto data update")
        data_list = self.cg.get_coins_markets(order='market_cap_desc', per_page=2, vs_currency='usd',
                                              price_change_percentage='1h,24h,7d,30d,1y', locale='en')
        await self.crypto_repo.add_many(convert_to_crypto_data(data_list))
