import unittest
from pathlib import Path
from market_data_core import MarketDataLocator, MarketDataError, MarketErrorCode, validate_metadata

class PublicCoreTests(unittest.TestCase):
    def test_valid_metadata(self):
        self.assertTrue(validate_metadata({"_schema_version": "v1", "data_type": "quote", "symbol": "DEMO"}))

    def test_missing_metadata(self):
        self.assertFalse(validate_metadata({"_schema_version": "v1"}))

    def test_wrong_version(self):
        self.assertFalse(validate_metadata({"_schema_version": "v2", "data_type": "quote", "symbol": "DEMO"}))

    def test_invalid_metadata_type(self):
        self.assertFalse(validate_metadata([]))

    def test_quote_path(self):
        self.assertEqual(MarketDataLocator(Path("sample")).quote("DEMO"), Path("sample/quote/latest/DEMO.json"))

    def test_candle_path(self):
        self.assertEqual(MarketDataLocator(Path("sample")).candles("DEMO", "day"), Path("sample/candles/day/DEMO.csv"))

    def test_traversal_rejected(self):
        for token in ("../secret", "a/b", "..", "", "a\\b"):
            with self.subTest(token=token):
                with self.assertRaises(ValueError):
                    MarketDataLocator(Path("sample")).quote(token)

    def test_invalid_frequency_rejected(self):
        with self.assertRaises(ValueError):
            MarketDataLocator(Path("sample")).candles("DEMO", "../secret")

    def test_error_code(self):
        error = MarketDataError(MarketErrorCode.SOURCE_TIMEOUT, "synthetic timeout")
        self.assertEqual(error.code, MarketErrorCode.SOURCE_TIMEOUT)

if __name__ == "__main__":
    unittest.main()
