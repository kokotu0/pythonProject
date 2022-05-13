
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

x=dataset.iloc[:,4]
y=dataset.iloc[:,10]
m=len(x)


theta0=1010;theta1=0

count=0
gradient_function_moving=[]
def gradient_function(theta0,theta1,alpha):
    global count
    count+=1

    H_x = theta0 + theta1 * x
    result_theta0=theta0-alpha*sum(np.array(H_x)-np.array(y))/m
    result_theta1=theta1-alpha*sum((np.array(H_x)-np.array(y))*np.array(x))/m
    print(result_theta0,result_theta1)

    if count==2000:

        return [result_theta0,result_theta1]
    else:
        return gradient_function(result_theta0,result_theta1,alpha=alpha)
def cost_function():
    pass


result=gradient_function(theta0,theta1,0.001)
plt.figure(1)
plt.scatter(x,y)
plt.plot(x,result[0]+result[1]*x,color='red')

plt.figure(2)

plt.show()