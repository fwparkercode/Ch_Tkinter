from tkinter import *
from tkinter import font
class App():
    def __init__(self, master):

        # declare variables
        self.n1 = DoubleVar()
        self.n2 = DoubleVar()
        self.total = DoubleVar()

        self.total.set(0.0)

        # Title
        self.title = Label(master, text="Award-Winning Addition App")
        self.title.grid(row=1, column=1, columnspan=2)

        # Add n1 label and entry widget
        self.n1_label = Label(master, text="Number 1:")
        self.n1_label.grid(row=2, column=1)

        self.n1_entry = Entry(master, textvariable=self.n1)
        self.n1_entry.grid(row=2, column=2)

        # Add n2 label and entry widget
        self.n2_label = Label(master, text="Number 2:")
        self.n2_label.grid(row=3, column=1)

        self.n2_entry = Entry(master, textvariable=self.n2)
        self.n2_entry.grid(row=3, column=2)

        # Total button and result label
        self.total_button = Button(master, text="Calculate", command=lambda:self.total.set(self.n1.get() + self.n2.get()))
        self.total_button.grid(row=4, column=1)

        self.total_label = Label(master, textvariable=self.total)
        self.total_label.grid(row=4, column=2)



if __name__ == "__main__":
    root = Tk()
    root.title("Add two numbers")
    my_app = App(root)
    root.mainloop()