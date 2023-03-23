# -*- coding: utf-8 -*-
"""Deliverable 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DAE6HGS_RV1HGqSrog5l-MX4xU1w_pnK
"""

import numpy as np

def random_list(size):
  list = []
  for i in range(size):
    list.append(np.random.randint(10, 50))
  return list

def sum_random(list):
  sum = 0
  for i in range(len(list)):
    sum = sum + list[i]
  return sum

while True:
  n = int(input("Enter an integer between 5 and 15: "))
  if n < 5 or n > 15:
    print("Invalid Input")
  else:
    break

print("Input: ", n)
list = random_list(n)
print("The elements of the random array are: ", list)
print("The sum is: ", sum_random(list))