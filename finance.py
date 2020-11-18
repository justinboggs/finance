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
csvName = input("Save csv as: ") + '.csv'
csvFileName = os.path.join(csvPath, csvName)

df.to_csv(csvFileName)

fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'], label=stock_name)
ax.set_ylabel('Price')
ax.set_xlabel('Date')
ax.set_title('Stocks')
plt.xticks(rotation=45)
fig.set_size_inches(18.5, 10.5)
plt.grid()
ax.legend(loc='upper left')
graphPath = 'data/stocks'
graphName = input('Save graph as: ') + '.png'
graphFileName = os.path.join(graphPath, graphName)
plt.savefig(graphFileName)

# graph = sns.lineplot(data=df, x="Date", y="Close")
# plt.xticks(rotation=45)
# plt.title(stock_name)
# plt.tight_layout()

# graphPath = 'data/stocks'
# graphName = input('Enter graph name: ') + '.png'
# graphFileName = os.path.join(graphPath, graphName)

# graph.figure.savefig(graphFileName)