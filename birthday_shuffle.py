from pfuncts import *
from sympy.utilities.iterables import multiset_permutations, variations
import numpy as np
import time

n = 9
pi_val = 5
a = np.arange(1, n + 1, 1, dtype=int)

start = time.perf_counter()
v = list(variations(a, n, True))
end = time.perf_counter()
print(f"Time to generate all n={n} variants: {end - start:0.4f} seconds")
print(f"# of possible variants: {len(v)}\n")

pfs = []

pfs_5 = []

start = time.perf_counter()
for i in v:
    if i[0] == pi_val:
        pfs_5.append(i)
end = time.perf_counter()
print(f"Time to find all pfs_5: {end - start:0.4f} seconds")
print(f"# of possible variations that start with {pi_val} : {len(pfs_5)}")

pfs_51 = []
start = time.perf_counter()
for i in pfs_5:
    if i[1] == 1:
        pfs_51.append(i)
end = time.perf_counter()
print(f"Time to find all variations that start with {pi_val}1: {end - start:0.4f} seconds")
print(f"# of possible PFs that start with {pi_val}1 : {len(pfs_51)}")

pfs_515 = []
start = time.perf_counter()
for i in pfs_51:
    if i[2] == 5:
        pfs_515.append(i)
end = time.perf_counter()
print(f"Time to find all variations that start with {pi_val}15: {end - start:0.4f} seconds")
print(f"# of possible PFs that start with {pi_val}15 : {len(pfs_515)}")

pfs_5159 = []
start = time.perf_counter()
for i in pfs_515:
    if i[3] == 9:
        pfs_5159.append(i)
end = time.perf_counter()
print(f"Time to find all variations that start with {pi_val}159: {end - start:0.4f} seconds")
print(f"# of possible PFs that start with {pi_val}159 : {len(pfs_5159)}")

pfs_51591 = []
start = time.perf_counter()
for i in pfs_5159:
    if i[4] == 1:
        pfs_51591.append(i)
end = time.perf_counter()
print(f"Time to find all variations that start with {pi_val}1591: {end - start:0.4f} seconds")
print(f"# of possible PFs that start with {pi_val}159 : {len(pfs_51591)}")

start = time.perf_counter()
for i in pfs_51591:
    if pigeonhole_check(i):
        pfs.append(i)
end = time.perf_counter()
print(f"Time to find all ParkingFunctions: {end - start:0.4f} seconds")
print(f"# of valid PFs with n={n} and start with {pi_val}1591: {len(pfs)}")

