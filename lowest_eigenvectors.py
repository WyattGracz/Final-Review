"""
This function calculates the eigenvalues of a square matrix and returns the values. 
It then arranges the eigenvalues and eigenvectors from smallest to largest. 
"""
__author__ = "Wyatt"


import numpy as np


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):

  m, n = square_matrix.shape
  
  if m != n:
    raise IndexError("Matrix is not square!")

  values, vectors = np.linalg.eig(square_matrix)
  values_sorted = np.sort(values)
  vectors_sorted = vectors[:, values.argsort()]

  return values_sorted[:number_of_eigenvectors+1], vectors_sorted[:number_of_eigenvectors+1]
