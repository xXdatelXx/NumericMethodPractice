from Practicums.Second.RootMethods import *
from Practicums.First.FunctionExploration import Explore
from sympy import sympify

expr = sympify(input("Write function:"))

print("Write scope (2 arguments):")
Explore(lambdify(symbols('x'), expr, 'numpy'), eval(input()), eval(input()))

print("Write root scope (2 arguments):")
a = eval(input())
b = eval(input())

print("Tol: 1e-4, Newton Root:", newton(expr, (a + b) / 2, 1e-4))
print("Tol: 1e-5, Newton Root:", newton(expr, (a + b) / 2, 1e-5))
print("Tol: 1e-6, Newton Root:", newton(expr, (a + b) / 2, 1e-6))

print("Tol: 1e-4, Simplified Newton Root:", simplified_newton(expr, (a + b) / 2, 1e-4))
print("Tol: 1e-5, Simplified Newton Root:", simplified_newton(expr, (a + b) / 2, 1e-5))
print("Tol: 1e-6, Simplified Newton Root:", simplified_newton(expr, (a + b) / 2, 1e-6))