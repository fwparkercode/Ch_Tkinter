#print(eval("3 * 3 + 5"))

'''
Making an awesome calculator
'''

from tkinter import *
from tkinter import font

class App():
    def __init__(self, master):
        self.current_string = StringVar() #store my equation
        self.current_string.set("")
        self.answer = DoubleVar() # store the result of equation
        self.answer.set(0)

        # Equation Label
        self.eqn = Label(master, textvariable=self.current_string, bg="black", fg="white", justify=RIGHT)
        self.eqn.grid(column=1, row=1, columnspan=4, sticky= "e" + "w")

        # add number buttons
        self.but1 = Button(master, text="1", command=lambda: self.current_string.set(self.current_string.get() + "1"))
        self.but1.grid(column = 1, row = 5)
        self.but2 = Button(master, text="2", command=lambda: self.current_string.set(self.current_string.get() + "2"))
        self.but2.grid(column=2, row=5)
        self.but3 = Button(master, text="3", command=lambda: self.current_string.set(self.current_string.get() + "3"))
        self.but3.grid(column=3, row=5)

        # add operator buttons
        self.but_add = Button(master, text="+", command=lambda: self.current_string.set(self.current_string.get() + "+"))
        self.but_add.grid(column=4, row=5)
        self.but_equal = Button(master, text="=", command=lambda: self.calc())
        self.but_equal.grid(column=4, row=6)

    def calc(self):
        eqn = self.current_string.get()
        answer = eval(eqn)
        self.current_string.set(str(answer))

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    app = App(root)
    root.mainloop()