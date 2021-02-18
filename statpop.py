import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

class StatPop:
    def __init__(self, url, stat_category, stat_column, color, kind):
        self.url = url
        self.stat_category = stat_category
        self.stat_column = stat_column
        self.color = color
        self.kind = kind

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
        data.plot(x="Season", 
                  y=self.stat_column, 
                  color=self.color, 
                  kind=self.kind,
                 figsize=(18.5, 10.5),
                 xticks=range(0, len(data["Season"])),
                rot=-80)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.legend(loc = 0, prop = {"size":25})
        start_loc=-0.25
        top_gap = max(data[self.stat_column])/100
        for number in data[self.stat_column]:
            plt.text(start_loc,number+top_gap,(str(number)),fontsize=15)
            start_loc+=1
        plt.show
        plt.savefig("statpop.png")
        return "DONE"

if __name__ == "__main__":
    statpop = StatPop("https://www.basketball-reference.com/players/c/cartevi01.html",
                    "per_game",
                    "PTS",
                    "skyblue",
                    "line")
    statpop.draw()