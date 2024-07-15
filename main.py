from tkinter import *


def mile_to_kilometer_convert():
    mile_value = float(miles_input.get())
    kilometer_value = round(mile_value * 1.609344)
    kilometers_number_label.config(text=f'{kilometer_value}')


# Window
window = Tk()
window.minsize(width=200, height=100)
window.title('Miles to Kilometer Converter')
window.config(padx=30, pady=30)

# Label for is equal to
equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label for number in kilometers
kilometers_number_label = Label(text='0')
kilometers_number_label.grid(column=1, row=1)


# Calculate Button
calculate_button = Button(text='Calculate', command=mile_to_kilometer_convert)
calculate_button.grid(column=1, row=2)

# Label for miles
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

# Label for kilometers
kilometers_label = Label(text='Km')
kilometers_label.grid(column=2, row=1)

window.mainloop()
