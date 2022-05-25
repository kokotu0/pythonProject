import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd
import numpy as np
import statistics
from matplotlib import pyplot
dataset=pd.DataFrame(pd.read_csv("C:/도소매업조사_음식숙박업(제공)_2016.csv",encoding='cp949'))
# print(dataset.iloc[0:,0])
# print(dataset.iloc[0:,7])
# print(dataset.iloc[0:,6])

earning_rate=np.array(dataset.iloc[0:,11])/np.array(dataset.iloc[0:,6])

print(earning_rate)
medain_value=(statistics.median(earning_rate))

# print(min(earning_rate))
# print(len(earning_rate))
count=0
for i,j in enumerate(earning_rate):
    if np.isnan(j)==True:
        print(i)
        print(dataset.iloc[0:,11][i])
        print(dataset.iloc[0:,6][i])
print(dataset.iloc[0:,11])
# print(count)
range_set=np.percentile(earning_rate,[1,99])
delete_set=[]
for i,j in enumerate(earning_rate):
    if j<range_set[0] or j >range_set[1]:
        delete_set.append(i)

dataset=dataset.drop(delete_set,axis=0)

earning_rate=np.array(dataset.iloc[0:,11])/np.array(dataset.iloc[0:,6])
plt.scatter(earning_rate,dataset.iloc[0:,0])
#
plt.show()