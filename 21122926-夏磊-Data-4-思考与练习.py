import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1

income=[1.47,1.62,1.78,1.94,2.38,2.60,2.82,3.07,3.21]
data=pd.DataFrame({'Income':income},index=['2012','2013','2014','2015','2016','2017','2018','2019','2020'])
data.plot(marker='s',linestyle=':',grid=True,xlim=(0,8),ylim=(0,3.5))
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('2012-2020年人均可支配收入')
plt.xlabel('Year',fontsize=12)
plt.ylabel('Income (RMB Ten Thousand)',fontsize=12)
plt.annotate('Largest!',xy=(8,3.21),xytext=(6.1,2.6),arrowprops=dict(arrowstyle='->'))
plt.savefig('2012-2020.jpg',dpi=400,bbox_inches='tight')
plt.show()

fig=plt.figure(figsize=(6,6))
plt.subplots_adjust(wspace=0.3,hspace=0.9)
ax1=fig.add_subplot(2,2,1)
data.plot(title='Line chart',fontsize='small',ax=ax1,xlabel='Year',ylabel='Income')
ax2=fig.add_subplot(2,2,2)
data.plot(kind='box',fontsize='small',ax=ax2,title='Box-whisker plot',xticks=[],ylabel='Income')
ax3=fig.add_subplot(2,1,2)
data.plot(kind='bar',use_index=True,fontsize='small',ax=ax3,xlabel='Year',ylabel='Income',title='Bar chart')
plt.show()

# 2
data2=pd.read_csv('High-speed rail.csv',index_col=0)
print(data2)
data2['Operation'].plot(kind='bar',rot=45,figsize=(9,6))
plt.title('Operation Mileage')
plt.ylabel('Mileage(km)',fontsize='small')
plt.xticks(fontsize='small')
plt.xlabel('Country',fontsize='small')
plt.show()
data2[['Operation','Under-construction','Planning']].plot(kind='barh',stacked=True)
plt.title('Global trends of high-speed rail')
plt.xlabel('Mileage(km)',fontsize='small')
plt.ylabel('Country',fontsize='small')
plt.yticks(fontsize='small')
plt.show()
data2['Operation'].plot(kind='pie',explode=[0.1,0,0,0,0,0],startangle=60,autopct='%1.1f%%')
plt.ylabel('')
plt.show()

