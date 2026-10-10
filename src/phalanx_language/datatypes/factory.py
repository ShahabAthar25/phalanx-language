from typing import Any, Callable

_float_contructor: Callable[[float], Any] | None = None


def register_float_contructor(constructor: Callable[[float], Any]):
    global _float_contructor
    _float_contructor = constructor


def make_float(value: float):
    if _float_contructor is None:
        raise RuntimeError("Float datatype has not been registered yet.")

    return _float_contructor(value)
