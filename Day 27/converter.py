from tkinter import *

def convert():
    km = input.get()
    miles = int(km) / 1.609
    output_label.config(text=f"{round(miles, 2)}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20,pady=20)

input = Entry(width=10)
# input.pack()
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

equal_label = Label(text="is equal to", font=("Arial", 14, "bold"))
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

output_label = Label(text="0", font=("Arial", 14, "bold"))
output_label.grid(column=1, row=1)
output_label.config(pady=10)

button = Button(text="Calculate", command=convert)
# button.pack()
button.grid(column=1, row=2)

window.mainloop()