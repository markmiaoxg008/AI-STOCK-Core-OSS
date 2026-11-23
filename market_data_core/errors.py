from enum import Enum

class MarketErrorCode(str, Enum):
    DATA_UNAVAILABLE = "DATA_UNAVAILABLE"
    SOURCE_TIMEOUT = "SOURCE_TIMEOUT"
    SCHEMA_MISMATCH = "SCHEMA_MISMATCH"
    INVALID_SYMBOL = "INVALID_SYMBOL"
    RATE_LIMITED = "RATE_LIMITED"

class MarketDataError(Exception):
    def __init__(self, code: MarketErrorCode, message: str):
        self.code = code
        super().__init__(message)
