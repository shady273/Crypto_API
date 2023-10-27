from src.utils.repository import SQLAlchemyRepository
from src.models.crypto_model import Crypto


class CryptosRepository(SQLAlchemyRepository):
    model = Crypto
