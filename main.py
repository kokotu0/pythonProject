
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
import datetime
import dateutil
#cost function -->시작위치 지정, theta 개수 지정(여기선 1차방정식으로만)
# gradient -->alpha값 지정

dataset=pd.DataFrame(pd.read_csv("C:/processed file.csv"))
A=pd.DataFrame([dataset.iloc[:,4],dataset.iloc[:,10]])
print(A)
x=dataset.iloc[:,4]
y=dataset.iloc[:,10]
plt.scatter(x,y)

plt.plot(x,x*0+1010,color='red')
# plt.show()
# dataset.to_csv("C:/Users/HAN/Downloads/processed file.csv",header=True)
#
# dataset=pd.DataFrame(pd.read_csv("C:/Users/HAN/Downloads/processed file.csv"))
# print(dataset)
#
# dataset['Formatted Date']=pd.to_datetime(dataset['Formatted Date'])
# print(type(dataset['Formatted Date'][0]))
# plt.xlabel('시간')
# plt.ylabel('온도(C)')
#
# x=dataset['Formatted Date']
# y=dataset['Apparent Temperature (C)']
#
# plt.scatter(dataset['Formatted Date'],dataset['Apparent Temperature (C)'],c='b',marker='o',s=0.5)
# plt.plot(,x*0.005+10)
plt.show()