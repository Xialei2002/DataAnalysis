import numpy as np
import pandas as pd

# 3.2
s1 = pd.Series([30, 25, 27, 41, 25, 34], index=["a", "b", "c", "d", "e", "f"])
print(s1)
s2 = pd.Series([27], index=["g"])
s1 = s1.append(s2)
print(s1)
s1["d"] = 40
print(s1)
print(s1[s1.values > 27])
s1 = s1.drop(s1.iloc[1:4].index)
print(s1)

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df1 = pd.DataFrame(arr1, index=["a", "b", "c"], columns=["one", "two", "three"], )
print(df1)
print(df1[["two", "three"]])
print(df1.iloc[0, :])
print(df1.iloc[2, :])
print(df1.iloc[:, 0])
print(df1.iloc[:, 2])
masks = df1["two"] > 2
data1 = df1.loc[masks, ["two"]]
print(data1)
data1["four"] = 10
print(data1)
masks2 = data1.values > 9
data1[masks2] = 8
print(data1)
# data1.loc[data1["two"]>9,"two"]=8
# data1.loc[data1["four"]>9,"four"]=8
# print(data1)
data1.drop(["b", "c"], axis=0, inplace=True)
print(data1)

# 3.3
narr = np.random.randint(10, 100, 350).reshape(50, 7)
df2 = pd.DataFrame(narr, columns=["a", "b", "c", "d", "e", "f", "g"])
print(df2)
df2.to_csv("out.csv", mode="w", header=True, index=False)
df3 = pd.read_csv("datingTestSet.csv", names=['flymiles', 'videogame', 'icecream', 'type'], skiprows=[0, 1])
print(df3.iloc[0:5, :])
masks3 = (df3['type'] == 'largeDoses')
print(df3.loc[masks3, :])

# 3.4
df4 = pd.read_excel("studentsInfo.xlsx", "Group1", index_col=0)
print(df4)
df4["案例教学"] = np.nan
df4 = df4.dropna(thresh=7)
print(df4)
df4 = df4.dropna(axis=1, thresh=1)
print(df4)

df5 = pd.read_excel("studentsInfo.xlsx", "Group1", index_col=0)
df5 = df5.fillna({'体重': df5['体重'].mean(), '成绩': df5['成绩'].mean()})
df5 = df5.fillna({'月生活费': df5['月生活费'].median()})
df5 = df5.fillna(method='ffill')
print(df5)

# 3.5
data0=pd.read_excel("studentsInfo.xlsx", "Group3", index_col=None)
print(data0)
data1=data0[["序号","性别","年龄"]]
print(data1)
data2=data0[["序号","身高","体重","成绩"]]
print(data2)
data1=pd.merge(data1,data2,how='inner',left_on="序号",right_on="序号")
print(data1)
data0=data0.sort_values(by="月生活费",ascending=True)
print(data0)
data0["成绩排名"]=data0["成绩"].rank(method='min',ascending=False)
print(data0)
