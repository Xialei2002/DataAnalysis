import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection, metrics,tree


def replace_num(a):
	j = 1
	for i in data[a].unique():
		data.loc[data[a] == i, a] = j
		j = j + 1


# 数据准备
data = pd.read_csv('income_census_train.csv', index_col=0)
data = data.dropna()
data = data.drop_duplicates()
data.drop('fnlwgt',axis=1,inplace=True)
replace_num('occupation')
replace_num('relationship')
replace_num('marital_status')
replace_num('workclass')
replace_num('gender')
data.loc[data['native_country'] != 'United-States', 'native_country'] = 'Non-United-States'

# 数据探索

pd.set_option('display.max_columns', None)
print(data.describe())

data['age'].plot(kind='box', figsize=(6, 6), title='Age')
plt.show()

data['income_bracket'].value_counts().plot(kind='pie',startangle=45,autopct='%1.1f%%',title='Income distribution',ylabel='income_bracket')
plt.show()

data[['hours_per_week', 'income_bracket']].groupby('hours_per_week').aggregate(np.mean).plot(marker='o',linestyle='dashed', title='Income varied by working time',rot=0)
plt.show()

data1=data.loc[data['income_bracket']==1,'education'].value_counts()
data2=data.loc[data['income_bracket']==0,'education'].value_counts()
fig=plt.figure(figsize=(8,4))
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
data1.plot(kind='bar',ax=ax1,title='High-income',ylabel='Number of person')
data2.plot(kind='bar',ax=ax2,title='Low-income')
plt.subplots_adjust(bottom=0.3,wspace=0.3)
plt.show()

data[['native_country', 'income_bracket']].groupby('native_country').aggregate(np.mean).plot(kind='bar', title='Income varied by Native-Country',rot=0)
plt.show()


# 建模预测
replace_num('education')
replace_num('race')
data.loc[data['native_country'] == 'United-States', 'native_country'] = 1
data.loc[data['native_country'] != 1, 'native_country'] = 2
y = data['income_bracket']
X = data.drop('income_bracket',axis=1)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)
clf=tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_train_pred=clf.predict(X_train)
y_test_pred=clf.predict(X_test)
train_err=metrics.mean_squared_error(y_train,y_train_pred)
test_err=metrics.mean_squared_error(y_test,y_test_pred)
print('测试/训练集RMSE：{:.2f},{:.2f}'.format(train_err,test_err))
print('决定系数：{:.2f}'.format(clf.score(X_test, y_test)))
