import polars as pl


class DataStore:
    def __init__(self) -> None:
        self._df: pl.DataFrame = pl.DataFrame()

    def load(self, df: pl.DataFrame) -> None:
        if not isinstance(df, pl.DataFrame):
            raise TypeError("DataStore requires a valid Polars DataFrame.")
        self._df = df

    def evaluate(self, expr: pl.Expr) -> pl.DataFrame | pl.Series:
        if self._df.is_empty():
            raise RuntimeError("Cannot evaluate expressions: DataStore is empty.")

        return self._df.select(expr)

    @property
    def is_empty(self) -> bool:
        return self._df.is_empty()
