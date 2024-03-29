# creating my first app using tkinter
import tkinter as tk
import ttkbootstrap as ttk


# functions for button functionalities
def Convert():
    the_input = entry_int.get()
    calculate = the_input * 1000
    output_string.set(calculate)


# creating window
window = ttk.Window()
# title of the window
window.title("Convertor")
# setting dimensions
window.geometry('300x150')
# creating the title of the application
title_label = ttk.Label(master=window, text='Kilometers to Meters', font='Calibri 24 bold')
title_label.pack()
# creating an input frame that has an entry section and a button
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=Convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)
# creating an output frame
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Answer', font='Calibri 24', textvariable=output_string)
output_label.pack(pady=5)

# creating the mainloop
window.mainloop()
