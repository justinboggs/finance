import investpy
from datetime import datetime
import pandas as pd
from prompt_toolkit import prompt
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt

stock_name = input('Symbol: ')

from_date = input('Start date (DD/MM/YYYY): ')

to_date = input('End date (DD/MM/YYYY): ')

df = investpy.get_stock_historical_data(stock=stock_name, country='United States', from_date=from_date, 
     to_date=to_date)

df.reset_index(inplace = True)

csvPath = 'data/stocks'
csvName = input("Enter file name: ") + '.csv'
csvFileName = os.path.join(csvPath, csvName)

df.to_csv(csvFileName)

graph = sns.lineplot(data=df, x="Date", y="Close")
plt.xticks(rotation=45)
plt.title(stock_name)
plt.tight_layout()

graphPath = 'data/stocks'
graphName = input('Enter graph name: ') + '.png'
graphFileName = os.path.join(graphPath, graphName)

graph.figure.savefig(graphFileName)