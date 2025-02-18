from FunctionExploration import Explore
from RootMethods import chord, secant, bisection

# Wrapper for RootMethods and FunctionExploration
class FunctionWrapper:
    def __init__(self, f):
        self.f = f

    def explore(self, start, end):
        Explore(self.f, start, end)

    def bisection(self, a, b, tol):
        return bisection(self.f, a, b, tol)

    def chord(self, a, b, tol):
        return chord(self.f, a, b, tol)

    def secant(self, a, b, tol):
        return secant(self.f, a, b, tol)
