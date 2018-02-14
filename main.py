import numpy as np
import matplotlib.pyplot as plt

# 讀取鳶尾花資料
# 花萼長, 花萼寬, 花瓣長, 花瓣寬, 花種編號 (山鳶尾花:1, 變色鳶尾花:2, 維吉尼亞鳶尾花:3)
data = np.genfromtxt('data\iris.csv', delimiter=',')

# 繪圖
fig = plt.figure()
sub = fig.add_subplot(211)

sub.plot(data[data[:,4]==1, 2], data[data[:,4]==1, 3], 'bd', alpha=0.2) #blue diamond
sub.plot(data[data[:,4]==2, 2], data[data[:,4]==2, 3], 'rs', alpha=0.2) #red square
sub.plot(data[data[:,4]==3, 2], data[data[:,4]==3, 3], 'go', alpha=0.2) #green o(circle)

# 設定圖標題
plt.title('Iris flower')

# 設定資料說明
plt.legend(['setosa', 'versicolor', 'virginica'], loc='upper left')

# 設定x軸及y軸標題
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')

# 設定隔線
plt.grid(True)

#--------------------------------
sub = fig.add_subplot(212)

sub.plot(data[data[:,4]==1, 0], data[data[:,4]==1, 1], 'bd', alpha=0.2) #blue diamond
sub.plot(data[data[:,4]==2, 0], data[data[:,4]==2, 1], 'rs', alpha=0.2) #red square
sub.plot(data[data[:,4]==3, 0], data[data[:,4]==3, 1], 'go', alpha=0.2) #green o(circle)

# 設定圖標題
plt.title('Iris flower')

# 設定資料說明
plt.legend(['setosa', 'versicolor', 'virginica'], loc='upper left')

# 設定x軸及y軸標題
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')

# 設定隔線
plt.grid(True)
#--------------------------------

# 繪圖
plt.show()
