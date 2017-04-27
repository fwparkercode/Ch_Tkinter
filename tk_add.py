from tkinter import *
from tkinter import font
from tkinter.ttk import *



class App():
    def __init__(self, master):
        s = Style()
        s.configure('BW.TLabel', foreground='red', background='light blue', borderwidth=3, justify=CENTER)
        self.title_font = font.Font(family="Comic Sans MS", size=40)
        self.widget_font = font.Font(family="Courier", size=30)
        print(font.families())
        # create variables
        self.n1 = DoubleVar() # IntVar, StringVar, BooleanVar
        self.n2 = DoubleVar()
        self.total = DoubleVar()

        self.n1.set(0)
        self.n2.set(0)
        self.total.set(0)
        print(self.n1.get())


        # Title
        self.title = Button(master, text="Award Winning App", style="BW.TLabel")
        self.title.grid(column=1, row=1, columnspan=2, sticky='w' + 'e', ipadx=20)

        # Number 1
        self.n1_label = Label(master, text="Number 1:", font=self.widget_font)
        self.n1_label.grid(column=1, row=2, sticky='e')

        self.n1_enter = Entry(master, textvariable=self.n1,font=self.widget_font, width=6, justify=CENTER)
        self.n1_enter.grid(column=2, row=2, sticky='w')

        # Number 2
        self.n2_label = Label(master, text="Number 2:",font=self.widget_font)
        self.n2_label.grid(column=1, row=3, sticky='e')

        self.n2_enter = Entry(master, textvariable=self.n2,font=self.widget_font, width=6, justify=CENTER)
        self.n2_enter.grid(column=2, row=3, sticky='w')

        # Calculate button
        self.calc_button = Button(master, text="Calculate", command=lambda:self.total.set(self.n1.get() + self.n2.get()),font=self.widget_font)
        self.calc_button.grid(column=1, row=4, sticky='e'+'w'+'n'+'s')

        # Total label
        self.total_label = Label(master, textvariable=self.total,font=self.widget_font, width=6, height=2, relief='raised')
        self.total_label.grid(column=2, row=4, sticky='e'+'w'+'n'+'s')




if __name__ == "__main__":
    root = Tk()
    my_app = App(root)
    root.mainloop()