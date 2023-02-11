# -*- coding: utf-8 -*-
"""CIS125_Lab2_Lloyd_Max_Quantization_s22212852.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tnyrhbwFG-MCfMt2_g5IQ1-fhsXdGiHy
"""

# Define the sampling range(start range, start value, end value)

x_start = 0
x_end = 1
sampling_rate = 44100
sample_num = (x_end - x_start) * sampling_rate
print(sample_num)

import numpy as np
x_values = np.linspace(x_start, x_end, sample_num)
print(x_values, len(x_values))

y_values = np.cos(x_values) + 0.5 * np.sin(x_values/2) + 0.5 * np.cos(x_values/4)
'''
Checked the behaviour for lecture note examples
#x_values = np.array([0,1,2,3,4])
#y_values = np.array([1.2,4.5,9.1,7.8,12.2])
'''
print(x_values, y_values)

import matplotlib.pyplot as plt
plt.plot(x_values, y_values)

# implement Quantization
bin_num = 8
min_value = np.min(y_values)
max_value = np.max(y_values)
print(min_value, max_value)

# Define Decision Boundary to calculate the centers
boundaries = np.linspace(min_value, max_value, bin_num+1)
print(boundaries, len(boundaries)) #here the boundaries includes the min and max value

# To determin the centeres
centers_w_boundaries = np.linspace(min_value, max_value, 2*bin_num+1)
print(centers_w_boundaries, len(centers_w_boundaries)) # this include center and the boundaries

# in order to remove the boundaries from the array
centers = centers_w_boundaries.copy()
index_list = []

for i in range(0, len(centers_w_boundaries)):
  for j in range(0, len(boundaries)):
    if centers_w_boundaries[i] == boundaries[j]:
      index_list.append(i)
      break
centers = np.delete(centers, index_list)
print(centers, len(centers)) # this can be used in the next code block (let's use the mean)

quantized_y_values = y_values.copy()
# measuring error
uniform_abs_error = 0

for y in range(0, len(y_values)):
  for b in range(0, len(boundaries)-1):
    #check whether boundes[b] <= y_yalues[y] <= boundaries[b+1]
    if y_values[y] >= boundaries[b] and y_values[y] <= boundaries[b+1]:
      # we just use (boundaries[b] + boundaries[b+1]) / 2 to be sure about the mean value
      quantized_y_values[y] = (boundaries[b] + boundaries[b+1]) / 2
      uniform_abs_error += abs(y_values[y] - (boundaries[b] + boundaries[b+1]) / 2)
      break


plt.plot(x_values, quantized_y_values)

# Lloyd Max Quantization
def lloydIteration(y_values, boundaries):
  bin_num = len(boundaries) - 1

  bin_sum_value = np.zeros(bin_num)
  bin_count = np.zeros(bin_num)

  for y in range(0, len(y_values)):
    for b in range (0, len(boundaries)-1):
      if y_values[y] >= boundaries[b] and y_values[y] <= boundaries[b+1]:
        bin_sum_value[b] += y_values[y]
        bin_count[b] += 1
  
  bin_value = bin_sum_value / bin_count

  #define new decision boundaries
  new_boundaries = boundaries.copy()
  # for 2nd item = mean (first and second centers) and so on
  new_boundaries[1:-1] = (bin_value[0:-1] + bin_value[1:])/2

  return new_boundaries

lloydIteration(y_values, boundaries)

'''
Result from 10 iteration
[1.26447129 1.29885394 1.33304234 1.36749998 1.40283698 1.43964021
 1.47777483 1.51024295 1.53029878]


Result from no further change (126 iteration)
[1.26447129 1.3053848  1.34531148 1.38405241 1.42133365 1.45674091
 1.48956556 1.515247   1.53029878]
'''

def lloydMaxOptimization(n: int):
  lloyd_boundaries = boundaries.copy()
  # in case user wants to get a specific number of loop
  if n > 0:
    for i in range(0,n):
      lloyd_boundaries=lloydIteration(y_values, lloyd_boundaries)
  
  # this part will run until no more change in boundaries
  elif n <= 0:
    prev_iter_lloyd_boundaries = np.zeros(len(boundaries))
    iter_count = 0
    identity_check = False
    
    while not identity_check:
      prev_iter_lloyd_boundaries = lloyd_boundaries.copy()
      lloyd_boundaries=lloydIteration(y_values, lloyd_boundaries)
      iter_count += 1
      
      for i in range (len(lloyd_boundaries)):
        if lloyd_boundaries[i] != prev_iter_lloyd_boundaries[i]:
          identity_check = False
          break
        else:
          identity_check = True

    print(f"Total number of iteration before reaching the final boundries: {iter_count}")
  
  return lloyd_boundaries

iteration_num = 10 # Integer: feel free to change the number of iteration 0 or negative for most optimal

lloyd_boundaries = lloydMaxOptimization(iteration_num)

print(lloyd_boundaries)

lloyd_quantized_y_values = y_values.copy()
lloydMax_abs_error = 0
for y in range(0, len(y_values)):
  for b in range(0, len(lloyd_boundaries)-1):
    #check whether boundes[b] <= y_yalues[y] <= boundaries[b+1]
    if y_values[y] >= lloyd_boundaries[b] and y_values[y] <= lloyd_boundaries[b+1]:
      lloyd_quantized_y_values[y] = (lloyd_boundaries[b] + lloyd_boundaries[b+1]) / 2
      lloydMax_abs_error += abs(y_values[y] - (lloyd_boundaries[b] + lloyd_boundaries[b+1]) / 2)
      break

# Quantize plot should be more ore less near the 
plt.plot(x_values, y_values, label = "Analog")
plt.plot(x_values, quantized_y_values, label = "Uniform Quant.")
plt.plot(x_values, lloyd_quantized_y_values, label = "Lloyd Max Quant.")
plt.legend()

# if we iteration is 126 -> abs error ~313
# Absolute Error Comparison
print(f"The absolute error of using Lloyd Max: {lloydMax_abs_error}")
print(f"The absolute error of using Uniform: {uniform_abs_error}")