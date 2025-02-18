from FunctionWrapper import FunctionWrapper
from numpy import sin  # Dont delete

# Realisation of first "NM" practicum

# Exercise 1:
print("Write function:")
f_string = input()


def f(x):
    return eval(f_string)


exercise = FunctionWrapper(f)

print("Write scope (2 arguments):")
exercise.explore(eval(input()), eval(input()))

# Exercise 2:
print("Write root scope (2 arguments):")
a = eval(input())
b = eval(input())

print("Tol: 1e-4, Bisection Root:", exercise.bisection(a, b, 1e-4))
print("Tol: 1e-5, Bisection Root:", exercise.bisection(a, b, 1e-5))
print("Tol: 1e-6, Bisection Root:", exercise.bisection(a, b, 1e-6))

print()

print("Tol: 1e-4, Chord Root:", exercise.chord(a, b, 1e-4))
print("Tol: 1e-5, Chord Root:", exercise.chord(a, b, 1e-5))
print("Tol: 1e-6, Chord Root:", exercise.chord(a, b, 1e-6))

print()

print("Tol: 1e-4, Secant Root:", exercise.secant(a, b, 1e-4))
print("Tol: 1e-5, Secant Root:", exercise.secant(a, b, 1e-5))
print("Tol: 1e-6, Secant Root:", exercise.secant(a, b, 1e-6))
