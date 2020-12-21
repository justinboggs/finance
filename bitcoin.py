import investpy
from datetime import datetime
import pandas as pd
from prompt_toolkit import prompt
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
from PIL import Image

from_date = input('Start date (DD/MM/YYYY): ')

to_date = input('End date (DD/MM/YYYY): ')

btc = investpy.get_crypto_historical_data(crypto='bitcoin', from_date=from_date, to_date=to_date)

btc.reset_index(inplace = True)

close_px = btc['Close']
btc['50d'] = close_px.rolling(window=50).mean()
btc['200d'] = close_px.rolling(window=200).mean()

csvPath = 'data/stocks'
csvName = input("Save csv as: ") + '.csv'
csvFileName = os.path.join(csvPath, csvName)
btc.to_csv(csvFileName)

fig, ax = plt.subplots()
ax.plot(btc['Date'], btc[['Close', '50d', '200d']])
ax.set_ylabel('Price')
ax.set_xlabel('Date')
ax.set_title('Bitcoin')
plt.xticks(rotation=45)
# plt.text(x=1970, y=400, s=r'Stock Price at this interval')
# ax.properties()['children'][0].set_color('black')
ax.properties()['children'][1].set_color('black')
ax.properties()['children'][2].set_color('purple')
fig.set_size_inches(18.5, 10.5)
plt.grid()
ax.legend(['Close', '50d', '200d'], loc='upper left')
ax.set_facecolor('xkcd:light grey')

graphPath = 'data/stocks'
graphName = input('Save graph as: ') + '.png'
graphFileName = os.path.join(graphPath, graphName)
plt.savefig(graphFileName)

img_PIL = Image.open(graphFileName)
img_PIL.show()
