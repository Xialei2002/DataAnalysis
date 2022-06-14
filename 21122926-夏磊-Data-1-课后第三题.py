studict={"A":170,"B":175,"C":180,"D":178,"E":172}
while(1):
	a=input()
	print(f"高于{a}同学身高的同学信息：")
	for i in studict.keys():
		if(studict[i]>studict[a]):
			print(i+':'+str(studict[i]))
	print("查找完成")