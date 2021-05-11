  
"""
This functioncreateas a column of data using the inputed quadratic fit( x and y arrays), 
then it creates plotable data and forms it back into an executable file for later use.
"""
__author__ = "Wyatt"

import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):

  if max_x < min_x:   
    raise ArithmeticError
  if number_of_points <= 2:   
    raise IndexError

  x_array = np.linspace(min_x, max_x, number_of_points) 
  y_array = np.polyval(quadratic_coefficients, x_array)
  fit_curve = np.array((x_array, y_array)) 

  return fit_curve