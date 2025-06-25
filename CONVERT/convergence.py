"""
This script compares the accuracy of the Backward Euler and Trapezoidal (Crank-Nicolson) methods for solving the ODE:
    dy/dt = a - b*y,   y(0) = y0
It includes:
- `analytical_solution(a, b, t)`: Returns the analytical solution at time(s) `t`.
- `backward_euler(a, b, y0, h, T)`: Solves the ODE using the Backward Euler method with step size `h` up to time `T`.
- `trapezoidal_method(a, b, y0, h, T)`: Solves the ODE using the Trapezoidal method with step size `h` up to time `T`.
- `compute_errors(a, b, y0, T, time_steps)`: Computes the maximum absolute error for both numerical methods over a range of time steps.
When run as a script, it:
- Sets up parameters for a stiff ODE problem.
- Computes errors for both methods over a range of time step sizes.
- Plots the maximum absolute error versus time step size on a log-log scale and saves the plot.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams.update({"font.size": 6})


def analytical_solution(a, b, t):
    return (a / b) * (1 - np.exp(-b * t))


def backward_euler(a, b, y0, h, T):
    y = y0
    ys = [y0]
    ts = [0.0]
    for n in range(int(T / h)):
        y = (y + h * a) / (1 + h * b)
        ys.append(y)
        ts.append((n + 1) * h)
    return np.array(ts), np.array(ys)


def trapezoidal_method(a, b, y0, h, T):
    y = y0
    ys = [y0]
    ts = [0.0]
    for n in range(int(T / h)):
        numerator = y * (1 - 0.5 * h * b) + h * a
        denominator = 1 + 0.5 * h * b
        y = numerator / denominator
        ys.append(y)
        ts.append((n + 1) * h)
    return np.array(ts), np.array(ys)


def compute_errors(a, b, y0, T, time_steps):
    be_errors = []
    trap_errors = []
    for h in time_steps:
        tt, ys_be = backward_euler(a, b, y0, h, T)
        tt, ys_trap = trapezoidal_method(a, b, y0, h, T)
        y_true = analytical_solution(a, b, tt)
        be_errors.append(np.max(np.abs(ys_be - y_true)))
        trap_errors.append(np.max(np.abs(ys_trap - y_true)))
    return be_errors, trap_errors


if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(__file__), "..", "PIC"))

    a = 1.0
    b = a * 20
    y0 = 0.0
    T = 10.0
    time_steps = [10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]

    be_errors, trap_errors = compute_errors(a, b, y0, T, time_steps)

    plt.figure(figsize=(6, 2))
    plt.loglog(time_steps, be_errors, "o-", label="Backward Euler")
    plt.loglog(time_steps, trap_errors, "s-", label="Trapezoidal")
    plt.xlabel(r"Time Step ($\Delta{}t$)")
    plt.ylabel(r"Absolute Error $|y_\text{num}-y_\text{ana}|$")
    plt.yscale("log")
    plt.xscale("log")
    plt.legend()
    plt.grid(True, which="major", ls="--")
    plt.tight_layout()
    plt.savefig("convergence.integration.pdf")
