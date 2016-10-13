import pandas as pd
import datetime
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "yahoo", start, end)

print df.head

style.use('fivethirtyeight')

df['Height'].plot
plt.legend()
plt.show()
