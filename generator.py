import sys
import threading
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from numpy import random
from pfuncts import pigeonhole_check


def save_location():
    """Defines a save file name and path"""
    now = datetime.now()
    date_string = now.strftime("%m-%d-%Y-%H-%M-%S")
    f_name = "generated_io_text_files/park_functions_generated/ParkingFunctions_" + date_string

    root.filename = filedialog.asksaveasfilename(title="Select Save Location",
                                                 initialdir=
                                                 "generated_io_text_files/park_functions_outcome",
                                                 initialfile=f_name, defaultextension=".csv",
                                                 filetypes=(("CSV files", "*.csv"),
                                                            ("all files", "*.*")))


def start_gen_thread():
    """Starts the thread for the generating function"""
    global GEN_THREAD
    finish_label.grid_remove()
    GEN_THREAD = threading.Thread(target=generate)
    GEN_THREAD.daemon = True
    gen_progress.grid()
    gen_progress.start(10)
    GEN_THREAD.start()
    root.after(20, check_gen_thread)


def check_gen_thread():
    """Check if thread work has completed"""
    if GEN_THREAD.is_alive():
        root.after(20, check_gen_thread)
    else:
        gen_progress.stop()
        gen_progress.grid_remove()
        finish_label.grid()


def generate():
    """Generates parking functions based on user input spinbox"""
    number_cars = n_spinbox.get()
    number_functions = i_spinbox.get()
    current_gen = []

    short_func_limit = True
    while short_func_limit:
        x = random.randint(1, int(number_cars) + 1, size=int(number_cars))
        if len(current_gen) >= int(number_functions):
            short_func_limit = False
        elif pigeonhole_check(x):
            current_gen.append(x)
            root.update_idletasks()

    now = datetime.now()
    date_string = now.strftime("%m-%d-%Y-%H-%M-%S")
    f_name = "generated_io_text_files/park_functions_generated/ParkingFunctions_" \
             + date_string + ".csv"
    with open(f_name, "w", encoding="utf8") as f:
        for x in current_gen:
            convert_arr = [str(element) for element in x]
            arr_str = ", ".join(convert_arr)
            f.write(arr_str + "\n")


def close():
    """Closes the GUI window"""
    root.destroy()
    sys.exit()


if __name__ == "__main__":
    root = Tk()
    root.geometry('420x200')
    root.title("Generate Parking Functions")

    n_cars = Label(root, text="Number of cars", font=("Arial Bold", 12))
    n_cars.grid(row=1, column=0)
    i_pks = Label(root, text="Number of PKs", font=("Arial Bold", 12))
    i_pks.grid(row=2, column=0, padx=30)
    n_spinbox = Spinbox(root, from_=1, to=10000, font=("Arial Bold", 12), justify="right", width=10)
    n_spinbox.grid(row=1, column=1)
    i_spinbox = Spinbox(root, from_=1, to=10000, font=("Arial Bold", 12), justify="right", width=10)
    i_spinbox.grid(row=2, column=1)
    gen_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
    gen_progress.grid(row=3, column=2, pady=20)
    gen_progress.grid_remove()
    finish_label = Label(root, text="Done!", font=("Arial Bold", 12))
    finish_label.grid(row=3, column=2)
    finish_label.grid_remove()
    btn_enter = Button(root, text="Generate", font=("Arial Bold", 13),
                       relief=RAISED, command=start_gen_thread,
                       bg="green", fg="white")
    btn_enter.grid(row=1, column=2, padx=10, pady=10, sticky="e", rowspan=2, ipady=20)
    btn_close = Button(root, text="Cancel", font=("Arial Bold", 13),
                       relief=RAISED, command=close, bg="red", fg="white")
    btn_close.grid(row=3, column=0, padx=10, pady=50, sticky="sw", ipady=10, ipadx=10)

    root.bind('<Return>', start_gen_thread)

    root.mainloop()
