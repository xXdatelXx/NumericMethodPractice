from Practicums.Second.RootMethods import *
from Practicums.First.FunctionExploration import Explore
from sympy import solve
import numpy as np

print("First exercise")

expr = input("Write phi:")

print("Write scope (2 arguments):")
Explore(lambdify(symbols('x'), expr, 'numpy'), eval(input()), eval(input()))

print("Write root scope (2 arguments):")
a = eval(input())
b = eval(input())

roots = solve(expr, symbols("x"))
if [root for root in roots if root.is_real]:
    print("Tol: 1e-4, Simply Iteration Root:", simple_iteration(expr, (a + b) / 2, 1e-4))
    print("Tol: 1e-4, Simply Iteration Root:", simple_iteration(expr, (a + b) / 2, 1e-5))
    print("Tol: 1e-4, Simply Iteration Root:", simple_iteration(expr, (a + b) / 2, 1e-6))
else:
    print("Dont have real roots")

coefficients = [1, -3, 9, -10]
roots = np.roots(coefficients)

for root in roots:
    print(root)

