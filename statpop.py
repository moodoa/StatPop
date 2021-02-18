import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

class StatPop:
    def __init__(self, url, stat_category, stat_column, color):
        self.url = url
        self.stat_category = stat_category
        self.stat_column = stat_column
        self.color = color

    def _collect_data(self, url, stat_category):
        text = requests.get(url).text
        soup = BeautifulSoup(text, "html.parser")
        pergame = soup.select_one(f"table#{stat_category}")
        data = pd.read_html(str(pergame))[0]
        career_idx = data[data["Season"]=="Career"].index[0]+1
        data = data.iloc[:career_idx]
        return data

    def draw(self):
        plt.style.use("fivethirtyeight")
        data = self._collect_data(self.url, self.stat_category)
        data.plot.bar(x = "Season", y=self.stat_column, color=self.color)
        plt.xticks(rotation=280)
        fig = plt.gcf()
        fig.set_size_inches(50, 30)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.legend(loc = 0, prop = {"size":35})
        start_loc=-0.25
        top_gap = max(data[self.stat_column])/100
        for number in data[self.stat_column]:
            plt.text(start_loc,number+top_gap,(str(number)),fontsize=25)
            start_loc+=1
        plt.show
        plt.savefig("statpop.png")
        return "DONE"

if __name__ == "__main__":
    statpop = StatPop("https://www.basketball-reference.com/players/c/cartevi01.html",
                    "per_game",
                    "PTS",
                    "skyblue")
    statpop.draw()