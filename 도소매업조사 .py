import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd
import numpy as np
import statistics
import matplotlib
import collections

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

matplotlib.rcParams['axes.unicode_minus'] = False


from matplotlib import pyplot
dataset=pd.DataFrame(pd.read_csv("C:/도소매업조사_음식숙박업(제공)_2016.csv",encoding='cp949'))


earning_rate=np.array(dataset.iloc[0:,11])/np.array(dataset.iloc[0:,6])

print(earning_rate)
medain_value=(statistics.median(earning_rate))

count=0
for i,j in enumerate(earning_rate):
    if np.isnan(j)==True:
        print(i)
        print(dataset.iloc[0:,11][i])
        print(dataset.iloc[0:,6][i])

delete_set=set()

earning_rate_range=np.percentile(earning_rate,[1,99])
employee_range=np.percentile(dataset.iloc[0:,0],[1,99])
revenue_range=np.percentile(dataset.iloc[0:,6],[1,99])

for i in range(len(earning_rate)):
    if earning_rate[i]<earning_rate_range[0] or earning_rate[i] > earning_rate_range[1]:
        delete_set.add(i)
    if dataset.iloc[0:,0][i]<employee_range[0] or dataset.iloc[0:,0][i]>employee_range[1]:
        delete_set.add(i)
    if dataset.iloc[0:,6][i]<revenue_range[0] or dataset.iloc[0:,6][i]>revenue_range[1]:
        delete_set.add(i)
    if np.isnan(dataset.iloc[0:,5][i]):delete_set.add(i)
dataset=dataset.drop(delete_set,axis=0)

earning_rate=np.array(dataset.iloc[0:,11])/np.array(dataset.iloc[0:,6])

# pyplot.suptitle('y축=매출액') '''변수간의 관계 확인 plot'''
# for i in range(0,12):
#     plt.subplot(3,4,i+1)
#     if i == 6:
#         plt.scatter(earning_rate,dataset.iloc[0:,6])
#         plt.title('영업이익률')
#         continue
#
#     plt.scatter(dataset.iloc[0:,i],dataset.iloc[0:,6])
#     plt.title(dataset.columns[i])
#
#
# # plt.show() plotting
x=pd.DataFrame(dataset.iloc[0:,:2])
x.insert(0,'x_0',np.ones(len(earning_rate)))
x.insert(3,'영업이익률',earning_rate)
x.insert(4,'건물합계면적',dataset.iloc[0:,5])
x.insert(5,'영업비용',dataset.iloc[0:,7])

# for i in range(0,5):
#     plt.subplot(2,3,i+1)
#     plt.scatter(x.iloc[0:,i],dataset.iloc[0:,6])
# plt.show()

# x.insert(5,)
# print(x.columns)


#Feature scaling 종사자수, 연간급여, 영업이익률, 건물합계면적, 영업비용(2,3,4,5,6)
#전처리 과정

x=x.reset_index()

def feature_scaling(dataframe,column_number):
    return dataframe.iloc[0:,column_number]/abs(max(dataframe.iloc[0:,column_number])-min(dataframe.iloc[0:,column_number]))
for i in [3,4,5,6]:
    x.iloc[0:,i]=feature_scaling(x,i)
x=x.drop(['index'],axis=1)


count=0
gradient_function_moving=[]
theta=np.array(np.zeros(len(x.columns)))

def J_theta(x=pd.DataFrame,theta=np.array,y=np.array):
    return sum(x@theta-y)**2 /len(y)

delete_set=[]
for i,j in enumerate(x.iloc[:,2]):
    if np.isnan(j):
        if x.iloc[i,1]<6:
            x.iloc[i,2]=0
        else:
            delete_set.append(i)

y=feature_scaling(dataset,6)
y=np.delete(np.array(y),delete_set)
x= x.drop(delete_set, axis=0);
x=x.reset_index(drop=True)
print(J_theta(x,theta,y))

#Gradient Descent
# def gradient_function(theta0,theta1,alpha):
#     global count
#     count+=1
#
#     H_x = theta0 + theta1 * x
#     result_theta0=theta0-alpha*sum(np.array(H_x)-np.array(y))/m
#     result_theta1=theta1-alpha*sum((np.array(H_x)-np.array(y))*np.array(x))/m
#     print(result_theta0,result_theta1)
#     gradient_function_moving.append(1/2/m*sum((np.array(H_x)-np.array(y))**2))
#     if count==2000:
#
#         return [result_theta0,result_theta1]
#     else:
#         return gradient_function(result_theta0,result_theta1,alpha=alpha)
#

#기본 theta 모음 ==> zero 벡터로

print()

#Normal Equation