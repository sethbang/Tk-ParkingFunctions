from pfuncts import *
from sympy.utilities.iterables import multiset_permutations, variations
import numpy as np
import time

n = 8
pi_val = 5
a = np.arange(1, n + 1, 1, dtype=int)

start = time.perf_counter()
v = list(variations(a, n, True))
end = time.perf_counter()
print(f"# of possible variants: {len(v)}")
print(f"Time to generate all n={n} variants: {end - start:0.4f} seconds")


p = []
pi_5 = []


for i in v:
    if i[0] == pi_val:
        pi_5.append(i)


pf_pi_5 = []

for i in pi_5:
    if pigeonhole_check(i):
        pf_pi_5.append(i)


print(f"\n# of possible variants with pi_1 = {pi_val}: {len(pi_5)}")
print(f"\n# of valid PFs with p1=5: {len(pf_pi_5)}")




