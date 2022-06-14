namelist = []
while 1:
	a = input()
	if len(namelist) == 0:
		namelist.append(a)
	else:
		b = True
		for i in namelist:
			if i == a:
				print("已在列表中:")
				print(namelist)
				b = False
		if b:
			namelist.append(a)
