from solver import solver
from exact import u_exact
import numpy as np
import matplotlib.pyplot as plt

def convergence_rates(m, solver_function, num_periods=8):
    from math import pi
    w = 0.31; I = 0.3
    P = 2*pi/w
    dt = P/30
    T = P*num_periods

    dt_values = []
    E_values = []
    for i in range(m):
        u, t = solver_function(I, w, dt, T)
        u_e = u_exact(t, I, w)
        E = np.sqrt(dt*np.sum((u_e-u)**2))
        dt_values.append(dt)
        E_values.append(E)
        dt = dt/2
        r = [np.log(E_values[i-1]/E_values[i])/
            np.log(dt_values[i-1]/dt_values[i])
            for i in range(1, m, 1)]
        return r, E_values, dt_values

def test_convergence_rates():
    r, E, dt = convergence_rates(
        m=5, solver_function=solver, num_periods=8
    )
    tol = 0.1
    assert abs(r[-1] - 2.0) < tol
    r, E, dt = convergence_rates(
        m=5, solver_function=solver, num_periods=8
    )
    print('adjust w rates: ', r)
    assert abs(r[-1] - 4.0) < tol

def plot_convergence_rates():
    r2, E2, dt2 = convergence_rates(
        m=5, solver_function=solver, num_periods=8
    )
    plt.loglog(dt2, E2)