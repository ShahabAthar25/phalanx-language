from phalanx_language.datatypes.vector import Vector


def builtin_shift(*args):

    if len(args) > 2:
        raise RuntimeError("Builtin function shift expects only 1 argument")

    series = args[0]
    offset = args[1]

    if not isinstance(series, Vector):
        raise RuntimeError("Expected series in shift")

    return Vector(series.value.shift(offset.value))
