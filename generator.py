import numpy as np
from numpy import random, loadtxt
from pfuncts import *
from datetime import datetime
from tkinter import *

root = Tk()

functions_list = []

user_choice = True

while user_choice:
    
    number_cars = input("\n\nEnter the number of cars/spots: ")

    number_functions = input("Enter the number of functions to generate: ")

    file_name = str(number_cars + "_" + str(number_functions) + "list")

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

    user_continue = input("Would you like to generate more functions (Y/N)? : ")

    if user_continue[0].upper() == 'N':
        user_choice = False
    
user_print = input("Would you like to print the generated functions to a text file (Y/N)? : ")

if user_print[0].upper() == 'Y':
    now = datetime.now()
    date_string = now.strftime("%m-%d-%Y-%H-%M-%S")
    f_name = "generated_io_text_files/park_functions_generated/" + str(len(functions_list)) + "_ParkingFunctions_" + date_string + ".csv"
    with open(f_name, "w") as f:
        for x in functions_list:
            convert_arr = [str(element) for element in x]
            arr_str = ", ".join(convert_arr)
            f.write(arr_str + "\n")
