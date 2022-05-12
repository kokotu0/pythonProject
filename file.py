import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dataset=pd.DataFrame(pd.read_csv("C:/Users/HAN/Downloads/processed file.csv"))
print(dataset)
dataset['Formatted Date']=pd.to_datetime(dataset['Formatted Date'])