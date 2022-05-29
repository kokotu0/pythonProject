import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd
import numpy as np
import statistics
import matplotlib

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

#'''Index(['종사자수_총소계', '연간급여_합계', '건물소유면적', '건물임차면적', '건물무상면적', '건물합계면적', '매출액',
#       '영업비용', '인건비', '임차료', '기타영업비용', '영업이익', '사업체승수', '종사자승수', '매출액승수'],
#     dtype='object')
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

# pyplot.suptitle('y축=매출액')
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

for i in range(0,5):
    plt.plot(2,3,i)
    plt.scatter(x.iloc[0:,i],dataset.iloc[0:6])
plt.show()
# x.insert(5,)
# print(x.columns)
theta=np.array(np.zeros(len(x.columns)))
print(x)
H_x=x*theta
print(H_x)
#Gradient Descent
    #Feature scaling

#Normal Equation