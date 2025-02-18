import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


# Function analysis, and graphics visualisation
def Explore(f, start, stop):
    # Set of points
    x_set = np.linspace(start, stop, 999)
    y_set = f(x_set)

    # Interpolation points
    zero_crossings = np.where(np.diff(np.sign(y_set)))[0]
    x0 = x_set[zero_crossings] - y_set[zero_crossings] * (x_set[zero_crossings + 1] - x_set[zero_crossings]) / (
            y_set[zero_crossings + 1] - y_set[zero_crossings])
    y0 = np.zeros_like(x0)

    # Derivative (f`(x))
    derivative = np.gradient(y_set, x_set)

    # Second Derivative (f``(x))
    second_derivative = np.gradient(derivative, x_set)

    # Antiderivative (F(x))
    antiderivative = np.vectorize(lambda x: quad(f, 0, x)[0])
    antiderivative_set = antiderivative(x_set)

    # Extrema points with Interpolation
    extrema_points = np.where(np.diff(np.sign(derivative)))[0]
    x_extrema = (x_set[extrema_points] - derivative[extrema_points] * (
            x_set[extrema_points + 1] - x_set[extrema_points]) /
                 (derivative[extrema_points + 1] - derivative[extrema_points]))
    y_extrema = f(x_extrema)

    # Visualisation
    plt.figure(figsize=(10, 6))

    # Graphics
    plt.plot(x_set, y_set, label='f(x)', color='blue')
    plt.plot(x_set, derivative, label="f'(x)", linestyle='dashed', color='red')
    plt.plot(x_set, second_derivative, label="f``(x)", linestyle='dashed', color='pink')
    plt.plot(x_set, antiderivative_set, label="F(x)", linestyle='dotted', color='green')

    # Points
    plt.scatter(x_extrema, y_extrema, color='black', label="Extrema")
    plt.scatter(x0, y0, color='red', zorder=5, label="Roots")

    # Legend
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Exploration of the function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
