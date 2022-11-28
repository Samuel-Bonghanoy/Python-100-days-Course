from tkinter import *

def button_clicked():
    new_label = input.get()
    my_label.config(text=f"{new_label}")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Sam is cool")
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)

# Button

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=2, row=0)

second_button = Button(text="Click Me Too", command=button_clicked)
second_button.grid(column=1, row=1)
# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)





window.mainloop()