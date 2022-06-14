import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import model_selection, metrics, tree

# 1
data = pd.read_csv('advertising.csv', index_col=0)
# print(data)
X = data.iloc[:, 0:3]
y = data.iloc[:, 3]
linreg = LinearRegression()
linreg.fit(X, y)
joblib.dump(linreg, 'linreg.pkl')
load_linreg = joblib.load('linreg.pkl')
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)
y_test_pred = linreg.predict(X_test)
err = metrics.mean_squared_error(y_test, y_test_pred)
predict_score = linreg.score(X_test, y_test)
print("全部数据RMSE:{:.2f}".format(err))
print('全部数据R^2:{:.2f}'.format(predict_score))
X_train2, X_test2, y_train2, y_test2 = model_selection.train_test_split(X, y, test_size=0.5, random_state=1)
linregTr=LinearRegression()
linregTr.fit(X_train2,y_train2)
y_tr_pr=linregTr.predict(X_train2)
y_te_pr=linregTr.predict(X_test2)
tr_err=metrics.mean_squared_error(y_train2,y_tr_pr)
te_err=metrics.mean_squared_error(y_test2,y_te_pr)
print('100-RMSE:{:.2f},{:.2f}'.format(tr_err,te_err))
print('score:{:.2f}'.format(linregTr.score(X_test2,y_test2)))

# 2
data2=pd.read_csv('bankdebt.csv',index_col=0,header=None)
data2.loc[data2[1]=='Yes',1]=1
data2.loc[data2[1]=='No',1]=0
data2.loc[data2[4]=='Yes',4]=1
data2.loc[data2[4]=='No',4]=0
data2.loc[data2[2]=='Single',2]=1
data2.loc[data2[2]=='Married',2]=2
data2.loc[data2[2]=='Divorced',2]=3
# print(data2)
Xtree=data2.loc[:,1:3]
ytree=data2.loc[:,4]
ytree=ytree.astype(int)
Xtree_train,Xtree_test,ytree_train,ytree_test=model_selection.train_test_split(Xtree,ytree,test_size=0.5,random_state=1)
clf=tree.DecisionTreeClassifier()
clf.fit(Xtree_train,ytree_train)
print(clf.score(Xtree_test,ytree_test))
clf2=tree.DecisionTreeClassifier()
clf2.fit(Xtree,ytree)
joblib.dump(clf2,'clf2.pkl')
load_clf2=joblib.load('clf2.pkl')
print(load_clf2.predict(Xtree))