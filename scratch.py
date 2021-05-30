# Jordan Winkler
# Sun May 30 10:01:36 EDT 2021

import sympy as sp
# simple integrals
from sympy.abc import *

x = sp.Symbol('x')
f = sp.integrate(x ** 2 + x + 1, x)

# line integrals, numerical
import autograd.numpy as np
from autograd import jacobian
from scipy.integrate import quad

def F(X):
    x, y, z = X
    return [y * np.exp(x), x**2 + np.exp(x), z**2 * np.exp(z)]

def C(t):
    return np.array([np.cos(t) + 1, np.sin(t) + 1, 1 - np.cos(t) - np.sin(t)])

dCdt = jacobian(C, 0)

def integrand(t):
    return F(C(t)) @ dCdt(t)

I, e = quad(integrand, 0, 2 * np.pi)
print(I, e)

