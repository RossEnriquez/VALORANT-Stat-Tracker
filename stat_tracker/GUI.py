import tkinter as tk
from tkinter import ttk
import fetch_data_GUI
from fetch_data_GUI import *

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        data = fetch_data_GUI.fetch('ross#vnsa', 'Unrated')
        #search bar
        self.enter = tk.Entry(self)
        self.enter.pack(side='top')

        # search button
        self.search = tk.Button(self)
        self.search["text"] = "SEARCH"
        self.search["command"] = self.find_player
        self.search.pack(side="top")

        #list of modes
        selected = tk.StringVar()
        self.mode_select = ttk.Combobox(root, textvariable=selected, width=1)
        self.mode_select['values'] = ('Unrated', 'Competitive', 'Spike Rush', 'Deathmatch')
        self.mode_select['state'] = 'readonly'
        self.mode_select.pack(fill='x', side='top')

        # stat label
        self.stats = tk.Label(self, justify='left')
        self.stats["text"] = f'\nWins:\nWin %:\n' \
                             f'Kills:\nDeaths:\n' \
                             f'Headshots:\n' \
                             f'Assists:\nFlawless:\nClutches:\n\n' \
                             f'Score/R:\nKills/R:\nDMG/R:\n' \
                             f'Most Kills in a Match:'
        self.stats.pack(side="left")

        #quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def find_player(self):
        try:
            user = self.enter.get()
            mode = self.mode_select.get()
            data = fetch_data_GUI.fetch(user, mode)
            print(data)
            self.stats["text"] = f'\nWins: {data[4][1]}\nWin %: {data[3][1]}\n' \
                                 f'Kills: {data[5][1]}\nDeaths: {data[7][1]}\n' \
                                 f'Headshots: {data[6][1]} ({data[2][1]}%)\n' \
                                 f'Assists: {data[8][1]}\nFlawless: {data[12][1]}\nClutches: {data[11][1]}\n\n' \
                                 f'Score/R: {data[9][1]}\nKills/R: {data[10][1]}\nDMG/R: {data[0][1]}\n' \
                                 f'Most Kills in a Match: {data[13][1]}'
        except TypeError:
            print('Please select a game mode!')
        except IndexError:
            print('Please enter a user name!')

root = tk.Tk()
app = GUI(master=root)
app.master.title("Hello World")
app.master.maxsize(500, 500)
app.master.minsize(500, 500)
app.master.geometry("500x500")

app.mainloop()