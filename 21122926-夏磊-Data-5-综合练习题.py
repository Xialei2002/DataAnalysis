import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import model_selection, metrics, tree

# wine
wine = pd.read_csv('wine.data', index_col=None, header=None)
# print(wine)
clf = tree.DecisionTreeClassifier()
X = wine.loc[:, 1:13]
y = wine.loc[:, 0]
y.astype(int)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

# house price
house = pd.read_excel('housePrice.xlsx', header=0, index_col=0)
# print(house)


house.loc[(house['电梯'] == '有'), '电梯'] = 1
house.loc[(house['电梯'] == '无'), '电梯'] = 0
house.loc[(house['所处层数'] == '低'), '所处层数'] = 1
house.loc[(house['所处层数'] == '中'), '所处层数'] = 2
house.loc[(house['所处层数'] == '高'), '所处层数'] = 3
house.loc[(house['建筑类型'] == '板楼'), '建筑类型'] = 1
house.loc[(house['建筑类型'] == '塔楼'), '建筑类型'] = 2
Xhp = house.iloc[:, [0, 1, 2, 3, 4, 7, 8, 9, 10, 16]]

yhp = house.iloc[:, -1]
print(Xhp)
print(yhp)
linreg = LinearRegression()
# Xhp_train,Xhp_test,yhp_train,yhp_test=model_selection.train_test_split(Xhp,yhp,test_size=0.35,random_state=1)
linreg.fit(Xhp, yhp)
predict_data=[[3,1,1,1,120,1,8,1,1,2010]]
print(f'预测价格：{linreg.predict(predict_data)[0]}万')
