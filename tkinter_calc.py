#print(eval("3 * 3 + 5"))

'''
Making an awesome calculator
'''

from tkinter import *
from tkinter import font
#from tkinter.ttk import *


class App():
    def __init__(self, master):
        # set fonts
        self.but_font = font.Font(family="kefa", size=30)

        # set vars
        self.current_string = StringVar() #store my equation
        self.current_string.set("")
        self.answer = DoubleVar() # store the result of equation
        self.answer.set(0)

        # Equation Label
        self.eqn = Label(master, textvariable=self.current_string, bg="black", fg="white", justify=RIGHT, font=self.but_font)
        self.eqn.grid(column=1, row=1, columnspan=4, sticky= "e" + "w")

        # add number buttons
        self.but1 = Button(master, text="1", command=lambda: self.current_string.set(self.current_string.get() + "1"), font=self.but_font)
        self.but1.grid(column = 1, row=5)
        self.but2 = Button(master, text="2", command=lambda: self.current_string.set(self.current_string.get() + "2"), font=self.but_font)
        self.but2.grid(column=2, row=5)
        self.but3 = Button(master, text="3", command=lambda: self.current_string.set(self.current_string.get() + "3"), font=self.but_font)
        self.but3.grid(column=3, row=5)

        # add operator buttons
        self.but_add = Button(master, text="+", command=lambda: self.current_string.set(self.current_string.get() + "+"), font=self.but_font)
        self.but_add.grid(column=4, row=5)
        self.but_equal = Button(master, text="=", command=lambda: self.calc(), font=self.but_font)
        self.but_equal.grid(column=4, row=6)

        #clear row2 col1
        self.but_clear = Button(master, text="C", command=lambda: self.current_string.set(""), font=self.but_font)
        self.but_clear.grid(row=2, column=1, sticky="n" + "e" + "s" + "w")
        self.lab_clear = Label(master, text="C")
        self.lab_clear.grid(row=2, column=1, sticky="n" + "e" + "s" + "w")

    def calc(self):
        eqn = self.current_string.get()
        answer = eval(eqn)
        self.current_string.set(str(answer))

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    app = App(root)
    root.mainloop()