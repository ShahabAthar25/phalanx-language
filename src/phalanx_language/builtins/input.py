from phalanx_language.datatypes.strings import String


def builtin_input(*args):
    val = input(*args)

    return String(val)
