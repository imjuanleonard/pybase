def fac(x: int) -> int:
    return 1 if x <= 1 else x * fac(x - 1)
