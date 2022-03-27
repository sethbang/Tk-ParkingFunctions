from tkinter import *
import numpy as np
from numpy import random, loadtxt
from pfuncts import *
import csv

pi = []
spec = []
non_desc = []
order_perm = []
inv_order_perm = []
parking_functions = []


def get_spec(pf):
    for x in range(len(pf)):
        spec.append(0)

    for i in range(len(pf)):
        index = pf[i] - 1
        element = spec[index]
        element += 1
        spec[index] = element
    return spec


def get_nondesc(s):
    nd = sorted(s)
    return nd


def get_ordperm(p, n):
    func_pi = p.copy()
    nd = n.copy()
    for i in range(len(func_pi)):
        v = func_pi[i]
        for j in range(len(nd)):
            if nd[j] == v:
                order_perm.append(j + 1)
                nd[j] = 0
                break
    return order_perm


def get_inv_ordperm(o):
    op = o.copy()
    iop = []
    for i in range(len(op)):
        for j in range(len(op)):
            if op[j] == i + 1:
                iop.append(j + 1)
    return iop


parking_functions = loadtxt("PFS.csv", dtype=int, delimiter=",", unpack=False)


# with open("PFS.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         inner_list = [int(elt.strip()) for elt in row.split(',')]
#         parking_functions.append(inner_list)


for x in parking_functions:
    print(f"{x}   --outcome-->  {get_outcome(x)[0]} with a displacement of {get_outcome(x)[1]}")
