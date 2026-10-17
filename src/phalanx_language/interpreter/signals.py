from phalanx_language.datatypes.base import Value


class ReturnSignal(Exception):
    def __init__(self, value: Value) -> None:
        self.value: Value = value
