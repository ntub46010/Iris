import numpy as np

data = np.genfromtxt('data/iris.csv', delimiter=',')

print(data)
print(type(data))
print('-' * 30)

#前50個
print(data[0:50])
print('-' * 30)

#從100開始到底
print(data[100:])
print('-' * 30)

#全部的第0個欄位
print(data[:,0])
print('-' * 30)

#全部的第0、1個欄位
print(data[:,[0, 1]])
print('-' * 30)

#前100個的第0、1個欄位
print(data[0:100,[0, 1]]) #前面的0可省略
print('-' * 30)

#全部第0個欄位的平均數
print(np.average(data[0:,0]))
print('-' * 30)

#全部第0個欄位的標準差
print(np.std(data[:,0]))
print('-' * 30)
