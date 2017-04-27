'''
Effort to make this look similar to OSX calculator with equation string shown
'''

from tkinter import *
from tkinter import font

class App():
    def __init__(self, master):
        button_color = "gray28"
        operator_color = "dark orange"

        self.current_string = StringVar()
        self.current_string.set("0")
        self.answer = DoubleVar()
        self.answer.set(0)
        self.my_font = font.Font(family="Helvetica Light", size=45)
        self.but_font = font.Font(family="Helvetica Light", size=23)

        # key bindings
        for i in range(10):
            master.bind(str(i), self.concat_bind)
        master.bind("+", self.concat_bind)
        master.bind("-", self.concat_bind)
        master.bind("x", self.concat_bind)
        master.bind("/", self.concat_bind)
        master.bind("<Return>", self.calc)

        # add number buttons
        Label(master, textvariable=self.current_string, width=10, bg="gray29", fg="white", font=self.my_font, anchor='e', pady=15).grid(column=1, row=1, columnspan=4)

        but1 = Label(master, text="1", bg='light gray', font=self.but_font, pady=10)
        but1.grid(column=1, row=5, sticky='nesw')
        but1.bind("<Button-1>", self.concat)
        but1.config(highlightbackground='dark gray', highlightthickness=1)


        but2 = Label(master, text="2", bg='light gray', font=self.but_font, pady=10)
        but2.grid(column=2, row=5, sticky='nesw')
        but2.bind("<Button-1>", self.concat)
        but2.config(highlightbackground='dark gray', highlightthickness=1)


        but3 = Label(master, text="3",bg='light gray', font=self.but_font, pady=10)
        but3.grid(column=3, row=5, sticky='nesw')
        but3.bind("<Button-1>", self.concat)
        but3.config(highlightbackground='dark gray', highlightthickness=1)


        but4 = Label(master, text="4",bg='light gray', font=self.but_font, pady=10)
        but4.grid(column=1, row=4, sticky='nesw')
        but4.bind("<Button-1>", self.concat)
        but4.config(highlightbackground='dark gray', highlightthickness=1)


        but5 = Label(master, text="5",bg='light gray', font=self.but_font, pady=10)
        but5.grid(column=2, row=4, sticky='nesw')
        but5.bind("<Button-1>", self.concat)
        but5.config(highlightbackground='dark gray', highlightthickness=1)


        but6 = Label(master, text="6",bg='light gray', font=self.but_font, pady=10)
        but6.grid(column=3, row=4, sticky='nesw')
        but6.bind("<Button-1>", self.concat)
        but6.config(highlightbackground='dark gray', highlightthickness=1)


        but7 = Label(master, text="7",bg='light gray', font=self.but_font, pady=10)
        but7.grid(column=1, row=3, sticky='nesw')
        but7.bind("<Button-1>", self.concat)
        but7.config(highlightbackground='dark gray', highlightthickness=1)


        but8 = Label(master, text="8",bg='light gray', font=self.but_font, pady=10)
        but8.grid(column=2, row=3, sticky='nesw')
        but8.bind("<Button-1>", self.concat)
        but8.config(highlightbackground='dark gray', highlightthickness=1)


        but9 = Label(master, text="9",bg='light gray', font=self.but_font, pady=10)
        but9.grid(column=3, row=3, sticky='nesw')
        but9.bind("<Button-1>", self.concat)
        but9.config(highlightbackground='dark gray', highlightthickness=1)


        but0 = Label(master, text="0", anchor='w',padx=25,bg='light gray', font=self.but_font, pady=10)
        but0.grid(column=1, row=6, columnspan=2, sticky='nesw')
        but0.bind("<Button-1>", self.concat)
        but0.config(highlightbackground='dark gray', highlightthickness=1)


        butplus = Label(master, text="+",bg=operator_color, fg='white', font=self.but_font, pady=10)
        butplus.grid(column=4, row=2, sticky='nesw')
        butplus.bind("<Button-1>", self.concat)
        butplus.config(highlightbackground='dark gray', highlightthickness=1)


        butminus = Label(master, text="-",bg=operator_color, fg='white', font=self.but_font, pady=10)
        butminus.grid(column=4, row=3, sticky='nesw')
        butminus.bind("<Button-1>", self.concat)
        butminus.config(highlightbackground='dark gray', highlightthickness=1)


        butmult = Label(master, text="x",bg=operator_color, fg='white', font=self.but_font, pady=10)
        butmult.grid(column=4, row=4, sticky='nesw')
        butmult.bind("<Button-1>", self.concat)
        butmult.config(highlightbackground='dark gray', highlightthickness=1)


        butdiv = Label(master, text="/",bg=operator_color, fg='white', font=self.but_font, pady=10)
        butdiv.grid(column=4, row=5, sticky='nesw')
        butdiv.bind("<Button-1>", self.concat)
        butdiv.config(highlightbackground='dark gray', highlightthickness=1)


        butequal = Label(master, text="=",bg=operator_color, fg='white', font=self.but_font, pady=10)
        butequal.grid(column=4, row=6, sticky='nesw')
        butequal.bind("<Button-1>", self.calc)
        butequal.config(highlightbackground='dark gray', highlightthickness=1)


        butdot = Label(master, text=".",bg='light gray', font=self.but_font, pady=10)
        butdot.grid(column=3, row=6, sticky='nesw')
        butdot.bind("<Button-1>", self.concat)
        butdot.config(highlightbackground='dark gray', highlightthickness=1)


        butclr = Label(master, text="C",bg='light gray', font=self.but_font, pady=10)
        butclr.grid(column=1, row=2, sticky='nesw')
        butclr.bind("<Button-1>", self.clear)
        butclr.config(highlightbackground='dark gray', highlightthickness=1)


        butlpar = Label(master, text="(",bg='light gray', font=self.but_font, pady=10)
        butlpar.grid(column=2, row=2, sticky='nesw')
        butlpar.bind("<Button-1>", self.concat)
        butlpar.config(highlightbackground='dark gray', highlightthickness=1)


        butrpar = Label(master, text=")",bg='light gray', font=self.but_font, pady=10)
        butrpar.grid(column=3, row=2, sticky='nesw')
        butrpar.bind("<Button-1>", self.concat)
        butrpar.config(highlightbackground='dark gray', highlightthickness=1)


        #self.answerlabel = Label(master, textvariable=self.answer).grid(column=0, row=5, columnspan=3)

    def concat(self, event):
        if self.current_string.get() == "0" or self.current_string.get()=="E":
            self.current_string.set("")
        self.current_string.set(self.current_string.get() + event.widget.cget("text"))
    def concat_bind(self, event):
        if self.current_string.get() == "0" or self.current_string.get()=="E":
            self.current_string.set("")
        self.current_string.set(self.current_string.get() + event.char)

    def calc(self, event):
        eqn = self.current_string.get()
        print(eqn)
        eqn = eqn.replace('x', '*')
        print(eqn)
        try:
            answer = str(eval(eqn))
        except:
            self.current_string.set("E")
        if len(answer) > 10:
            answer = answer[:10]
        self.answer.set(answer)
        self.current_string.set(str(answer))
    def clear(self, event):
        self.current_string.set("")



if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    app = App(root)
    root.mainloop()
