"""
CST-305 Project 1 – Visualize ODE With SciPy

Programmers: Hiyaw Ertiro, Ashton Calkins

Packages Used:
- numpy
- scipy (scipy.integrate.solve_ivp)
- matplotlib

Approach to Implementation:
This program models server queue performance using a first-order ordinary differential equation:
dx/dt = λ − μx. The user provides system parameters (arrival rate, service efficiency, initial
queue size, and simulation time). The ODE is solved numerically using SciPy’s Runge–Kutta
solver (solve_ivp). The solution is visualized to show queue size over time, along with the
analytically computed steady-state queue length. The results are interpreted in the context
of system stability and overload behavior.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

print("=== Server Queue Performance Model ===")
print("Differential equation: dx/dt = λ − μx")
print("This models the number of requests in a server queue over time.\n")

#inputs
lam = float(input("Enter request arrival rate λ (requests/sec): "))
mu = float(input("Enter service efficiency μ (1/sec): "))
x0 = float(input("Enter initial queue size x(0) (requests): "))
t_end = float(input("Enter simulation time (seconds): "))

def queue_model(t, x):
    return lam - mu * x

t_eval = np.linspace(0, t_end, 500)

#give the solution
solution = solve_ivp(
    queue_model,
    (0, t_end),
    [x0],
    t_eval=t_eval,
    rtol=1e-6,
    atol=1e-8
)

x_ss = lam / mu

#print and plot the solution
plt.plot(solution.t, solution.y[0], label="Queue Size x(t) (requests)")
plt.axhline(x_ss, linestyle="--", color="red", label=f"Steady-State: {x_ss:.2f} requests")
plt.xlabel("Time (seconds)")
plt.ylabel("Queue Size (number of requests)")
plt.title("Server Queue Performance Over Time")
plt.legend()
plt.grid(True)
plt.show()

#performance metrics
print("\n=== Performance Summary ===")
print(f"Simulation Time: 0 to {t_end} seconds")
print(f"Initial Queue Size: {x0} requests")
print(f"Request Arrival Rate λ: {lam} requests/sec")
print(f"Service Efficiency μ: {mu} 1/sec")
print(f"Computed Steady-State Queue: {x_ss:.2f} requests")
print(f"Numerical Solver Relative Error Tolerance: 1e-6")
print(f"Numerical Solver Absolute Error Tolerance: 1e-8")
print("\nInterpretation: The queue will stabilize near the steady-state value. "
      "If λ > μ * x, the queue grows (overload). If μ * x > λ, the queue shrinks (stable system).")

