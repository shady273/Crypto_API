from src.repository.crypto import CryptosRepository
from src.services.crypto import CryptoServices


def crypto_service():
    return CryptoServices(CryptosRepository)
