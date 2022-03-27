from pfuncts import *
from sympy.utilities.iterables import multiset_permutations, variations
import numpy as np
import time
from numpy import random, loadtxt
from datetime import datetime

n = 100
num_arrays = 10000
functions_list = []
run = True
a = np.arange(1, n + 1, 1, dtype=int)

number_cars = input("\n\nEnter the number of cars/spots: ")

number_functions = input("Enter the number of functions to generate: ")
start = time.perf_counter()
number_cars = n

number_functions = num_arrays

x = random.randint(1, int(number_cars) + 1, size=(int(number_functions), int(number_cars)))

current_gen = []
num_succ_functions = 0
for i in x:
    if pigeonhole_check(i):
        current_gen.append(i)
num_succ_functions = len(current_gen)
print(str(num_succ_functions) + " of " + str(number_functions) + " generated functions were valid.")
suc_rate = (float(num_succ_functions) / float(number_functions)) * 100
print(f"That is a {suc_rate:0.4f}% success rate.")

functions_list.extend(current_gen)
print(f"You have generated {len(functions_list)} PFs total.")
end = time.perf_counter()
print(f"Time to find all parking functions when n={n} variants: {end - start:0.4f} seconds")
