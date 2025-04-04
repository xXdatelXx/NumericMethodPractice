from sympy import symbols, lambdify, diff


def newton(expr, x, tol):
    x_sym = symbols('x')
    f = lambdify(x_sym, expr, 'numpy')
    df = lambdify(x_sym, diff(expr, x_sym), 'numpy')

    while abs(f(x)) > tol:
        if df(x) == 0:
            return "Method does not match"

        x = x - f(x) / df(x)

    return x


def simplified_newton(expr, x, tol):
    x_sym = symbols('x')
    f = lambdify(x_sym, expr, 'numpy')
    df = lambdify(x_sym, diff(expr, x_sym), 'numpy')
    df = df(x)

    if df == 0:
        return "Method does not match"

    while abs(f(x)) > tol:
        x = x - f(x) / df

    return x


def simple_iteration(expr, x0, tol, max_iter=100):
    phi = lambdify(symbols('x'), expr, 'numpy')

    x = x0
    for _ in range(max_iter):
        x_new = phi(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new

    raise ValueError("Method does not match")
