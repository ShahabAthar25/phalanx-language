from phalanx_language.datatypes.null import Null


def builtin_println(*args) -> Null:
    print(*args)
    return Null()
