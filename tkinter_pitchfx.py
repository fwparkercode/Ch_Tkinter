from tkinter import *
from tkinter import font
import urllib
from bs4 import BeautifulSoup
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt






class App():
    '''Builds the tkinter app to select game'''
    def __init__(self, master, url):
        '''
        :param master: root for this App
        :param url: landing page for brooks baseball
        '''


        self.title = Label(text="Brooks Baseball PitchFX Data\nChoose a Game", bg="dark blue", fg="white").grid(column=0, row=0, columnspan=3)
        # select from lists
        self.url = url
        self.page = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.page.read(), "html.parser")

        # make a frame to contain selectors
        self.group = LabelFrame(master, text="Select your game and pitcher", padx=5, pady=5, bg="light blue")
        self.group.grid(column=0, row=1, columnspan=3, rowspan=5, sticky="w" + "e")

        self.month_list, self.month_numlist = self.get_list(url, "month")
        self.month_var = StringVar()
        self.month_var.set(self.month_list[0])
        self.month_drop = OptionMenu(master, self.month_var, *self.month_list).grid(column=0,row=1)

        self.day_list, x = self.get_list(url, "day")
        self.day_var = StringVar()
        self.day_var.set(self.day_list[0])
        self.day_drop = OptionMenu(master, self.day_var, *self.day_list).grid(column=1,row=1)

        self.year_list, x = self.get_list(url, "year")
        self.year_var = StringVar()
        self.year_var.set(self.year_list[0])
        self.year_drop = OptionMenu(master, self.year_var, *self.year_list).grid(column=2, row=1)




        self.submit_date_button = Button(master, text="Select Date", command=lambda:self.submit_date(master, self.month_numlist[get_index(self.month_list, self.month_var)], self.day_var.get() ,self.year_var.get()))
        self.submit_date_button.grid(column=0,row=2)

    def submit_date(self, master, month, day, year):
        '''
        Choose the date of your game from 3 dropdowns
        :param master: root
        :param month: month as string number
        :param day: day as string number
        :param year: year as string number
        '''
        self.submit_date_button.destroy()

        self.url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=%s&day=%s&year=%s&prevDate=43&league=mlb" % (month, day, year)
        print(self.url)
        self.page = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.page.read(),"html.parser")
        self.game_list, self.gameid_list = self.get_list(self.url, "game")
        self.game_var = StringVar()
        longest = 0
        longesti = 0
        for i in range(len(self.game_list)):
            if len(self.game_list[i]) > longest:
                longest = len(self.game_list[i])
                longesti = i
        self.game_var.set(self.game_list[longesti])
        self.game_drop = OptionMenu(master, self.game_var, *self.game_list).grid(column=0, row=3, columnspan=3)
        self.game_submit_button = Button(master, text="Select Game", command=lambda:self.submit_game(master, self.month_numlist[get_index(self.month_list, self.month_var)], self.day_var.get() ,self.year_var.get(), self.gameid_list[get_index(self.game_list, self.game_var)]))
        self.game_submit_button.grid(column=0, row=5)

    def submit_game(self, master, month, day, year, game):
        '''
        Choose the game to view
        :param master: root
        :param month: month numberstring
        :param day: day numberstring
        :param year: year numberstirng
        :param game: gameid from brooks baseball
        '''
        self.game_submit_button.destroy()
        self.url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=%s&day=%s&year=%s&game=%s&prevDate=53&league=mlb" % (month, day, year, game)
        print(self.url)
        self.page = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.page.read(), "html.parser")
        self.pitcher_list, self.pitcherid_list = self.get_list(self.url, "pitchSel")
        self.pitcher_var = StringVar()
        print(self.pitcher_list)
        self.pitcher_var.set(self.pitcher_list[0])
        self.pitcher_drop = OptionMenu(master, self.pitcher_var, *self.pitcher_list).grid(column=0, row=6, columnspan=3)
        #self.submit_date_button.destroy()
        self.pitcher_submit_button = Button(master, text="Select Pitcher", command=lambda:self.select_pitcher(master, self.month_numlist[get_index(self.month_list, self.month_var)], self.day_var.get() ,self.year_var.get(), self.gameid_list[get_index(self.game_list, self.game_var)], self.pitcherid_list[get_index(self.pitcher_list, self.pitcher_var)]))
        self.pitcher_submit_button.grid(column=0, row=7)

    def select_pitcher(self, master, month, day, year, game, pitcher):
        '''
        Select pitcher from selected game
        :param master: root
        :param month: string of month number
        :param day: string of day number
        :param year: string of year number
        :param game: gid from brooks baseball
        :param pitcher: pitcherid from brooks
        '''
        #self.pitcher_submit_button.destroy()
        self.url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=%s&day=%s&year=%s&game=%s&pitchSel=%s&league=mlb" % (month, day, year, game, pitcher)
        print(self.url)
        self.page = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.page.read(), "html.parser")

        self.plotter = Ploty(game, pitcher)


    def get_list(self, url, name):
        '''
        Take the url with the new dropdown, and return the labels and values
        :param url: 
        :param name: 
        :return: label_list and val_list, (val list is used for new url, label is used for display only) 
        '''
        my_label_list = [x.text.strip() for x in self.soup.find("select", {"name": name}).findAll("option")]
        my_val_list = [x['value'] for x in self.soup.find("select", {"name": name}).findAll("option")]
        print(my_val_list)
        return my_label_list, my_val_list



class Ploty():
    '''
    object to manage the plot through matplotlib
    '''
    def __init__(self, game, pitcher):
        '''
        Pass game and pitcher to go straight to brooks game data page for that pitcher and day
        :param game: 
        :param pitcher: 
        '''
        self.link = "http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel=%s&game=%s" % (pitcher, game)
        self.page = urllib.request.urlopen(self.link)
        self.soup = BeautifulSoup(self.page.read(), "html.parser")
        print(self.soup.prettify())
        self.headers = [x.text.strip() for x in self.soup.find("table").find("tr").findAll("th")]

        self.data = [[y for y in x.findAll("td")] for x in self.soup.find("table").findAll("tr")]
        self.data = self.data[1:]
        for i in range(len(self.headers)):
            print(i, "=", self.headers[i], ":", self.data[0][i])
        print(self.data[0])

        # pull the x, y data
        self.x_data = [float(x[-6].text.strip()) for x in self.data]
        self.y_data = [float(x[-5].text.strip()) for x in self.data]

        self.x_strike = [float(x[-6].text.strip()) for x in self.data if x[9].text.strip() == "S"]
        self.y_strike = [float(x[-5].text.strip()) for x in self.data if x[9].text.strip() == "S"]
        print(self.x_strike)
        self.x_ball = [float(x[-6].text.strip()) for x in self.data if x[9].text.strip() == "B"]
        self.y_ball = [float(x[-5].text.strip()) for x in self.data if x[9].text.strip() == "B"]

        self.x_inplay = [float(x[-6].text.strip()) for x in self.data if x[9].text.strip() == "X"]
        self.y_inplay = [float(x[-5].text.strip()) for x in self.data if x[9].text.strip() == "X"]

        self.x = [float(x[-6].text.strip()) for x in self.data]
        self.y = [float(x[-5].text.strip()) for x in self.data]
        self.type = [x[15].text.strip() for x in self.data]

        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111)

        for i in range(len(self.x)):
            ax.annotate(str(self.type[i]), xy=(self.x[i], self.y[i]), horizontalalignment='center', verticalalignment='center')

        #plot the pitches
        #plt.scatter(self.x_data, self.y_data)
        plt.scatter(self.x_inplay,self.y_inplay, color="b", s=200, alpha=0.5)
        plt.scatter(self.x_ball, self.y_ball, color="g", s=200, alpha=0.5)
        plt.scatter(self.x_strike, self.y_strike, color="r", s=200, alpha=0.5)


        plt.title(my_app.pitcher_var.get() + "\n" + my_app.game_var.get() + "\n" + my_app.month_var.get() + " " + my_app.day_var.get() + ", " + my_app.year_var.get())

        #draw an approximate strike zone
        x_strike = [-17 / 12 / 2, 17 / 12 / 2]
        y_top_strike = [3.3, 3.3]
        y_bottom_strike = [1.49, 1.49]

        y_vert_strike = [1.49, 3.3]
        x_vert_strike_left = [-17 / 12 / 2, -17 / 12 / 2]
        x_vert_strike_right = [17 / 12 / 2, 17 / 12 / 2]

        plt.plot(x_strike,y_top_strike, "r--")
        plt.plot(x_strike,y_bottom_strike, "r--")
        plt.plot(x_vert_strike_left,y_vert_strike, "r--")
        plt.plot(x_vert_strike_right,y_vert_strike, "r--")

        plt.xlabel("Horizontal Pitch Location (ft)")
        plt.ylabel("Vertical Pitch Location (ft)")

        plt.axis("equal")
        plt.xlim([-2.5, 2.5])
        plt.ylim([0, 5])


        plt.tight_layout()


        plt.show()


def get_index(list, option_value):
    return list.index(option_value.get())


if __name__ == "__main__":

    url = "http://www.brooksbaseball.net/pfxVB/pfx.php"
    root = Tk()
    root.title("Brooks PitchFX")

    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=18)
    my_app = App(root, url)
    root.mainloop()
