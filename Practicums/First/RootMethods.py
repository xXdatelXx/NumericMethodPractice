def bisection(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return "Method requires a change of sign on [a, b]"

    while abs(b - a) > 2 * tol:
        c = (a + b) / 2
        a, b = (a, c) if f(a) * f(c) < 0 else (c, b)
    return (a + b) / 2


def chord(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return "Method requires a change of sign on [a, b]"

    while abs(b - a) > tol:
        c = b - f(b) * (b - a) / (f(b) - f(a))
        a, b = (a, c) if f(a) * f(c) < 0 else (c, b)
    return c


def secant(f, a, b, tol):
    while abs(b - a) > tol:
        c = b - f(b) * (b - a) / (f(b) - f(a))
        a, b = b, c
    return b
