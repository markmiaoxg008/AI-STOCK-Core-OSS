from collections.abc import Mapping

SCHEMA_VERSION = "v1"
REQUIRED = ("_schema_version", "data_type", "symbol")

def validate_metadata(value: object) -> bool:
    if not isinstance(value, Mapping):
        return False
    if value.get("_schema_version") != SCHEMA_VERSION:
        return False
    return all(isinstance(value.get(key), str) and bool(value[key].strip()) for key in REQUIRED)
