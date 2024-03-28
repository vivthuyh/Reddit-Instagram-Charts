import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv('redditinsta.csv')

plt.rcParams["figure.figsize"] = [7.50,3.50]
plt.rcParams["figure.autolayout"] = True

fig, axs = plt.subplots(2)
fig.suptitle('Reddit Instagram Likes and Comments in Jan.2024')
axs[0].plot(data['Date'],data['Likes'])
axs[1].plot(data['Date'],data['Comments'])

fig.autofmt_xdate()
plt.xticks(np.arange(0,66, step=3))
plt.xlabel('Date')
plt.ylabel('Likes(Top) & Comments(Bottom)')

plt.show()