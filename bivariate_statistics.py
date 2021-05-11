"""
Calculates things based on given data
"""
__author__ = "Wyatt"

import numpy as np
from scipy import stats

def bivariate_statistics(data):
  
  if (len(data)!=2 or len(data[0])<=1): 
    raise IndexError

  stat = stats.describe(data)
  x_min, x_max = stat.minmax[0][0], stat.minmax[1][0]
  y_min, y_max = stat.minmax[0][1], stat.minmax[1][1]
  meany = stat.minmax[0][1]
  standard_deviation_of_y = np.sqrt(stat.variance[1])
  statistics = np.array([meany, standard_deviation_of_y, x_min, x_max, y_min, y_max])
  return statistics


