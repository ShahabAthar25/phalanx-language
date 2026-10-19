import polars as pl

from phalanx_language.datatypes.asset import Asset
from phalanx_language.datatypes.strings import String


def builtin_load_data(*args):
    if len(args) < 2:
        raise RuntimeError(
            "Builtin function 'load_data' expects 2 arguments: symbol and file_path."
        )

    symbol = args[0]
    file_path = args[1]

    if not isinstance(symbol, String) or not isinstance(file_path, String):
        raise RuntimeError(
            "Arguments to 'load_data' must be strings: (symbol, file_path)"
        )

    try:
        df = pl.read_csv(file_path.value)
    except Exception as e:
        raise RuntimeError(
            f"Failed to read CSV file for asset '{symbol}' at '{file_path}': {e}"
        )

    # Close column is required
    if "close" not in df.columns:
        raise RuntimeError(
            f"Asset '{symbol}' is missing the mandatory 'close' column. "
            f"Found columns: {df.columns}"
        )

    # Return the wrapped Asset runtime value
    return Asset(value=df, symbol=symbol)
