from dataclasses import dataclass

import polars as pl

from phalanx_language.datatypes.base import Value
from phalanx_language.datatypes.vector import Vector


# self.value will perform mutations as series are stored in vectors datatype
# and the series is linked to the df to minimize ram usage. Thus frozen=False
@dataclass(frozen=False, slots=True)
class Asset(Value):
    value: pl.DataFrame
    symbol: str

    def type_name(self) -> str:
        return "asset"

    def is_truthy(self) -> bool:
        return self.value.height != 0

    def __str__(self) -> str:
        row_count = self.value.height
        cols = ", ".join(self.value.columns)
        return f"<Asset symbol='{self.symbol}', rows={row_count}, columns=[{cols}]>"

    def add_col(self, name: str, series: pl.Series):
        self.value = self.value.with_columns(pl.Series(name, series))
        return self.value

    def has_column(self, name: str) -> bool:
        return name in self.value.columns

    def get_attribute(self, name: str) -> Vector:
        if name in self.value.columns:
            series = self.value.get_column(name)
            return Vector(value=series)

        raise AssertionError(f"No attribute with the name of {name}")
