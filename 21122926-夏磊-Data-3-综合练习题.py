import numpy as np
import pandas as pd

# 1
df1 = pd.read_excel("DataScience.xls", "Sheet1", index_col=None)
print(df1[["实验项目名称"]])
print(f"总数：{df1.index.max() + 1}")
masks1 = df1.isnull().any(axis=1)
df2 = df1.loc[masks1, :]
print(df2)
df2.to_csv("pre.csv", mode='w', header=True, index=True)
df1 = df1.dropna(thresh=1)
df1 = df1.fillna(method='ffill')
print(df1.loc[masks1, :])
print(df1[["课程名称", "实验项目名称", "实验类型", "二级实验室名称"]])
for i in df1["课程名称"].unique():
	print(f"{i}实验课时数：", df1.loc[(df1["课程名称"] == i), "实验课时数"].sum())
# sjjg=(df1["课程名称"]=="数据结构")
# sjwj=(df1["课程名称"]=="数据挖掘与机器学习")
# sjkx=(df1["课程名称"]=="数据科学导论")
# pysj=(df1["课程名称"]=="Python语言程序设计")
# dsj=(df1["课程名称"]=="大数据技术")
# swsj=(df1["课程名称"]=="商务数据分析")
# print("数据结构实验课时数：",df1.loc[sjjg,"实验课时数"].sum())
# print("数据挖掘与机器学习实验课时数：",df1.loc[sjwj,"实验课时数"].sum())
# print("数据科学导论实验课时数：",df1.loc[sjkx,"实验课时数"].sum())
# print("Python语言程序设计实验课时数：",df1.loc[pysj,"实验课时数"].sum())
# print("大数据技术实验课时数：",df1.loc[dsj,"实验课时数"].sum())
# print("商务数据分析实验课时数：",df1.loc[swsj,"实验课时数"].sum())
# print("数据结构实验类型分布：\n",df1.loc[sjjg,"实验类型"].value_counts())
# print("数据挖掘与机器学习实验类型分布：\n",df1.loc[sjwj,"实验类型"].value_counts())
# print("数据科学导论实验类型分布：\n",df1.loc[sjkx,"实验类型"].value_counts())
# print("Python语言程序设计实验类型分布：\n",df1.loc[pysj,"实验类型"].value_counts())
# print("大数据技术实验类型分布：\n",df1.loc[dsj,"实验类型"].value_counts())
# print("商务数据分析实验类型分布：\n",df1.loc[swsj,"实验类型"].value_counts())
# print(df1.loc[(df1["班级"]=="数据科学181"),:])
# print(df1.loc[(df1["班级"]=="数据科学(卓越)171"),:])
# print(df1.loc[(df1["班级"]=="数据科学182"),:])
# print(df1.loc[(df1["班级"]=="数据科学(卓越)191"),:])
# print(df1.loc[(df1["班级"]=="大数据应用171"),:])
# print(df1.loc[(df1["班级"]=="数据科学171"),:])
# print(df1.loc[(df1["班级"]=="大数据应用191"),:])
# print(df1.loc[(df1["班级"]=="数据科学172"),:])
for i in df1["班级"].unique():
	print(f"{i}班课表：\n", df1.loc[(df1["班级"] == i), :])
for i in df1["二级实验室名称"].unique():
	print(f"{i}承担课时数：", df1.loc[(df1["二级实验室名称"] == i), "实验课时数"].sum())
for i in df1["二级实验室名称"].unique():
	print(f"{i}能承担实验类型：", df1.loc[(df1["二级实验室名称"] == i), "实验类型"].unique())

# 2
df3 = pd.read_csv("bankpep.csv")
print(df3)
print("储户总数：", df3["id"].count())
for i in df3["region"].unique():
	print(f"{i}储户数：", df3.loc[(df3["region"]) == i, "id"].count())
for i in df3["sex"].unique():
	print(f"{i}收入均值：", df3.loc[(df3["sex"] == i), "income"].var(), f"\n{i}收入方差：", df3.loc[(df3["sex"] == i), "income"].var())
for i in df3["sex"].unique():
	print(f"{i}接收新业务数：\n", df3.loc[(df3["sex"] == i), "pep"].value_counts())
for i in df3["region"].unique():
	print(f"{i}接受新业务数：\n", df3.loc[(df3["region"] == i), "pep"].value_counts())
df3.loc[(df3["save_act"] == "NO"), "save_act"] = 0
df3.loc[(df3["save_act"] == "YES"), "save_act"] = 1
df3.loc[(df3["pep"] == "NO"), "pep"] = 0
df3.loc[(df3["pep"] == "YES"), "pep"] = 1
grouped=df3.groupby(["pep","save_act"])
print(grouped.aggregate({"income":np.mean}))
