from tkinter import *
from tkinter import filedialog
import numpy as np
from numpy import random, loadtxt
from datetime import datetime
from pfuncts import *
import pprint

root = Tk()
root.title('Parking Function List Selection')
root.filename = filedialog.askopenfilename(
    initialdir="generated_io_text_files/park_functions_generated", title="Select A File",
    filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
# Change the file name here to match the csv file you wish to analyze
pf_input_filename = root.filename


pi = []

non_desc = []

inv_order_perm = []


def get_spec(pf):
    spec = []
    for x in range(len(pf)):
        spec.append(0)

    for i in range(len(pf)):
        index = pf[i] - 1
        element = spec[index]
        element += 1
        spec[index] = element
    return spec


def get_nondesc(p):
    s = p.copy()
    nd = sorted(s)
    return nd


def get_ordperm(p):
    order_perm = []
    nd = get_nondesc(p)
    func_pi = p.copy()
    for i in range(len(func_pi)):
        v = func_pi[i]
        for j in range(len(nd)):
            if nd[j] == v:
                order_perm.append(j + 1)
                nd[j] = 0
                break
    return order_perm


def get_inv_ordperm(o):
    op = get_ordperm(o)
    iop = []
    for i in range(len(op)):
        for j in range(len(op)):
            if op[j] == i + 1:
                iop.append(j + 1)
    return iop


parking_functions = loadtxt(pf_input_filename, dtype=int, delimiter=",", unpack=False)


now = datetime.now()
date_string = now.strftime("%m-%d-%Y-%H-%M")
f_name = str(len(parking_functions)) + "_ParkFunctsOutput_" + date_string

root.filename = filedialog.asksaveasfilename(title="Select Save Location",
                                             initialdir="generated_io_text_files/park_functions_outcome",
                                             initialfile=f_name, defaultextension=".txt",
                                             filetypes=(("text files", "*.txt"), ("all files", "*.*")))

with open(root.filename, "a") as f:
    for x in parking_functions:
        f.write("\n\n")
        this_function_dict = {
                "original": list(x),
                "n": len(x),
                "isPF": pigeonhole_check(x),
                "outcome": get_outcome(x)[0],
                "displacement": get_outcome(x)[1],
                "specification": get_spec(x),
                "non-descending": get_nondesc(x),
                "order_permutation": get_ordperm(x),
                "inv-order-permutation": get_inv_ordperm(x)
        }
        pprint.pprint(this_function_dict, indent=4, width=100, sort_dicts=False, stream=f)

root.mainloop()
