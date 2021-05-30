# Jordan Winkler
# Sun May 30 10:01:36 EDT 2021

import sympy as sp
# simple integrals
from sympy.abc import *

x = sp.Symbol('x')
f = sp.integrate(x ** 2 + x + 1, x)

# solving
from sympy.solvers import solve 
sp.solve = solve
import z3

# solve assumes arg1 = 0
## This solver is also naked of units
## sp.solve can also choke on hard equations
sp.solve(x**2 - 1, x) 
sp.solve(x - y, x) 

# z3 has bounds control, and types
x = z3.Int('x')
y = z3.Int('y')
z3.solve(x > 2, y < 10, x + 2*y == 7)

from z3 import *
# internal representation of reals is precise
# these are not amateur floats, actual reals
x = Real('x')
y = Real('y')
solve(x**2 + y**2 > 3, x**3 + y < 5)

# if you want a SAT instead of SMT you can just use Bool
p = Bool('p')
q = Bool('q')
r = Bool('r')
solve(Implies(p, q), r == Not(q), Or(Not(p), r))

x = Int('x')
y = Int('y')
# a whole z3 program can be written from python
s = Solver()
s.add(x > 10, y == x + 2)
print(s)
print("Solving constraints in the solver s ...")
print(s.check())

print("Create a new scope...")
s.push()
s.add(y < 11)
print(s)
print("Solving updated set of constraints...")
print(s.check())

print("Restoring state...")
s.pop()
print(s)
print("Solving restored set of constraints...")
print(s.check())

# line integrals, numerical
#import autograd.numpy as np
#from autograd import jacobian
#from scipy.integrate import quad
#
#def F(X):
#    x, y, z = X
#    return [y * np.exp(x), x**2 + np.exp(x), z**2 * np.exp(z)]
#
#def C(t):
#    return np.array([np.cos(t) + 1, np.sin(t) + 1, 1 - np.cos(t) - np.sin(t)])
#
#dCdt = jacobian(C, 0)
#
#def integrand(t):
#    return F(C(t)) @ dCdt(t)
#
#I, e = quad(integrand, 0, 2 * np.pi)
#print(I, e)
#
