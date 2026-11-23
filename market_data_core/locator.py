import re
from pathlib import Path

_TOKEN = re.compile(r"[A-Za-z0-9_-]{1,64}\Z")

class MarketDataLocator:
    def __init__(self, root: Path):
        self.root = Path(root)

    @staticmethod
    def _token(value: str) -> str:
        if not isinstance(value, str) or not _TOKEN.fullmatch(value):
            raise ValueError("invalid path token")
        return value

    def quote(self, symbol: str) -> Path:
        return self.root / "quote" / "latest" / (self._token(symbol) + ".json")

    def candles(self, symbol: str, frequency: str) -> Path:
        return self.root / "candles" / self._token(frequency) / (self._token(symbol) + ".csv")
