from tkinter import *

windows = Tk()
windows.title("Miles to KM converter")
windows.config(padx=20, pady=20)

def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_meter_result.config(text=f"{km}") # i need o/p in string so we use f string


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


miles_lables = Label(text="Miles")
miles_lables.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_meter_result = Label(text="0")
kilo_meter_result.grid(column=1, row=1)

k_m_label = Label(text="K.M.")
k_m_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

windows.mainloop()