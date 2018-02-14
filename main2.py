import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 讀取鳶尾花資料
# 花萼長, 花萼寬, 花瓣長, 花瓣寬, 花種編號 (山鳶尾花:1, 變色鳶尾花:2, 維吉尼亞鳶尾花:3)
data = np.genfromtxt('data\iris.csv', delimiter=',')

#資料洗牌
np.random.shuffle(data)
#print(data)

X = data[:120, [0,1,2,3]]
y = data[:120, 4]
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y) #開始學習

d = data[120:, [0,1,2,3]]
predict = knn.predict(d)
correct = data[120:, 4]

for i in range(30):
    if predict[i] == correct[i]:
        print('O')
    else:
        print('X')
