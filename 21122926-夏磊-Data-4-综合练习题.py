import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('bankpep.csv',index_col=0)
data.loc[(data["save_act"]=='NO'),"save_act"]=0
data.loc[(data["save_act"]=='YES'),"save_act"]=1
data.loc[(data["current_act"]=='NO'),"current_act"]=0
data.loc[(data["current_act"]=='YES'),"current_act"]=1
data.loc[(data["mortgage"]=='NO'),"mortgage"]=0
data.loc[(data["mortgage"]=='YES'),"mortgage"]=1
data.loc[(data["pep"]=='NO'),"pep"]=0
data.loc[(data["pep"]=='YES'),"pep"]=1
data.loc[(data["married"]=='NO'),"married"]=0
data.loc[(data["married"]=='YES'),"married"]=1
data.loc[(data["car"]=='NO'),"car"]=0
data.loc[(data["car"]=='YES'),"car"]=1
print(data)
data['age'].plot(kind='hist',bins=10,density=True,title='Customer Age')
data['age'].plot(kind='kde',style='k--')
plt.xlabel('Age')
plt.show()

data.plot(kind='scatter',x='age',y='income',xlabel='Age',ylabel='Income',title='Customer Income',xlim=(0,80),label='(age,income)')
plt.legend(loc='upper left')
plt.show()

pd.plotting.scatter_matrix(data[['age','income','children']],diagonal='hist')
plt.show()

grouped=data.groupby('region')
mean=grouped['income'].mean()
std=grouped['income'].std()
mean.plot(kind='bar',yerr=std,title='Customer Income',rot=45)
plt.xticks(fontsize='small')
plt.xlabel('Region',fontsize='small')
plt.show()

fig=plt.figure(figsize=(6,6))
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
data1=data.groupby('sex')['income'].aggregate(np.sum)
data1.plot(kind='pie',autopct='%1.1f%%',ylabel='Sex',startangle=45,ax=ax1,title='Customer Sex')
data2=data.loc[(data['car']==1),:].groupby(['sex'])['income'].aggregate(np.sum)
data2.plot(kind='pie',autopct='%1.1f%%',ylabel='Sex',startangle=45,ax=ax2,title='Customer Car Sex')
data3=data.groupby('children')['income'].aggregate(np.sum)
data3.plot(kind='pie',autopct='%1.1f%%',ylabel='Children',startangle=45,ax=ax3,title='Customer Children')
plt.show()

data[['sex','income']].boxplot(by='sex',figsize=(6,6))
plt.title('income')
plt.show()
