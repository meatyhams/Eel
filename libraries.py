# libraries
# simple graphical elements
import matplotlib.pyplot as plt

# numerical calulations
import numpy as np

# symbolic calculations 
import sympy as sp
from sympy.abc import * # skip declaring symbols, eats up namespace though
#!pip install magpylib

# SMT solver 
import z3

# packaged EM 
import magpylib as em

# Neural network stuff 
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

# working with:
# - lists with special operators and functors
# -- Dirac delta (1d, 3d), dot, cross, (gradient, div, curl), line integral, base-change, tensors
