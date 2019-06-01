import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt 
from torch.autograd import Variable
input_size = 1
output_size = 1
learning_rate = 0.001
#使用xtrain產生矩陣資料
xtrain = np.array([[2.3], [4.4], [6.3], [4.8], [50.6], [3.6], [14.6], [42.6], [35.6], [43.6], [32.4], [98.5]], dtype=np.float32)
#使用ytrain產生矩陣資料
ytrain = np.array([[4.4], [53.86], [5.4] , [45.2], [43.09], [5.67] ,[60.6], [4.52], [433.6], [4.6], [43.4],[4.3]], dtype.np.float32)
#進行繪圖
plt.figure()
plt.scatter(xtrain,ytrain)
#x軸命名
plt.xlable('x軸')
#y軸命名
plt.ylable('y軸')
#顯示圖片
plt.show()


