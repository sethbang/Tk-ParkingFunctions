from tkinter import *
import numpy as np
from pfuncts import *

window = Tk()
window.title("Parking Functions")
window.geometry("800x800")
top_frame = Frame(window, relief=SUNKEN, borderwidth=5, pady=10)
top_frame.pack(fill=X)
input_frame = Frame(window, borderwidth=5, pady=10)
input_frame.pack(fill=X)
result_frame = Frame(window, relief=SUNKEN, borderwidth=5, pady=10)
result_frame.pack(fill=X)

pi = []

non_desc = []
order_perm = []
inv_order_perm = []

e = Entry(input_frame, width=20, font=("Arial Bold", 18))
e.grid(row=0, column=0, pady=10)


def add_click(number):
    new_nums = number.split(',')
    for x in new_nums:
        pi.append(int(x))
    # pi.append(int(number))
    pf_full.config(text=str(pi))
    e.delete(0, END)


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


def result_click():
    the_spec = get_spec(pi)
    spec_result.config(text=str(the_spec))
    non_desc = get_nondesc(pi)
    ndesc_result.config(text=str(non_desc))
    order_perm = get_ordperm(pi, non_desc)
    op_result.config(text=str(order_perm))
    inv_order_perm = get_inv_ordperm(order_perm)
    iop_result.config(text=str(inv_order_perm))
    result_outcome = get_outcome(pi)
    outcome_result.config(text=str(result_outcome[0]))
    displacement_result.config(text=str(result_outcome[1]))


pf_label = Label(top_frame, text="Parking Function: ", font=("Arial Bold", 18))
pf_label.grid(row=0, column=0)
pf_full = Label(top_frame, text=str(pi), font=("Arial Bold", 18))
pf_full.grid(row=0, column=1, sticky="w")

btn_add = Button(input_frame, text="Add to pi", font=("Arial Bold", 12), bg="green", fg="white",
                 command=lambda: add_click(e.get()))

btn_add.grid(row=0, column=1, padx=5, sticky="e")

btn_enter = Button(input_frame, text="GET RESULTS", font=("Arial Bold", 12), bg="blue", fg="white",
                   relief=RAISED, command=result_click)

btn_enter.grid(row=1, column=0, sticky="w")

result_label = Label(result_frame, text="RESULTS", font=("Arial Bold", 18))
result_label.grid(row=0, column=1)

div_label = Label(result_frame, text="=========================", font=("Arial Bold", 18))
div_label.grid(row=1, column=1, sticky="w")

spec_label = Label(result_frame, text="Specification: ", font=("Arial Bold", 12))
spec_label.grid(row=2, column=0, pady=15, sticky="e")
spec_result = Label(result_frame, text="", font=("Arial", 12))
spec_result.grid(row=2, column=1, pady=15, sticky="w")

ndesc_label = Label(result_frame, text="Non-descending: ", font=("Arial Bold", 12))
ndesc_label.grid(row=3, column=0, pady=15, sticky="e")
ndesc_result = Label(result_frame, text="", font=("Arial", 12))
ndesc_result.grid(row=3, column=1, pady=15, sticky="w")

op_label = Label(result_frame, text="Order Permutation: ", font=("Arial Bold", 12))
op_label.grid(row=4, column=0, pady=15, sticky="e")
op_result = Label(result_frame, text="", font=("Arial", 12))
op_result.grid(row=4, column=1, pady=15, sticky="w")

iop_label = Label(result_frame, text="Inverse Order Permutation: ", font=("Arial Bold", 12))
iop_label.grid(row=5, column=0, pady=15, sticky="e")
iop_result = Label(result_frame, text="", font=("Arial", 12))
iop_result.grid(row=5, column=1, pady=15, sticky="w")

outcome_label = Label(result_frame, text="Outcome: ", font=("Arial Bold", 12))
outcome_label.grid(row=6, column=0, pady=15, sticky="e")
outcome_result = Label(result_frame, text="", font=("Arial", 12))
outcome_result.grid(row=6, column=1, pady=15, sticky="w")

displacement_label = Label(result_frame, text="Displacement: ", font=("Arial Bold", 12))
displacement_label.grid(row=7, column=0, pady=15, sticky="e")
displacement_result = Label(result_frame, text="", font=("Arial", 12))
displacement_result.grid(row=7, column=1, pady=15, sticky="w")

window.mainloop()
