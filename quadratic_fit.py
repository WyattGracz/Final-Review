  
"""
This function takes an array and does stuff
"""
__author__ = "Wyatt"


import numpy as np


def quadratic_fit(array):
  
  x_values = array[0, :] 
  y_values = array[1, :] 

  quadratic_coefficients = np.polyfit(x_values, y_values, 2)

  return quadratic_coefficients