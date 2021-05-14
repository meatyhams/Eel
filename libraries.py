# libraries
import matplotlib.pyplot as plt
import numpy as np
 
import sympy as sp
from sympy.abc import * # skip declaring symbols, eats up namespace though
#!pip install magpylib
import magpylib as em
 
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils


