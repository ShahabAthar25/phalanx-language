from phalanx_language.datatypes.null import Null


def println(*args) -> Null:
    print(*args)
    return Null()
