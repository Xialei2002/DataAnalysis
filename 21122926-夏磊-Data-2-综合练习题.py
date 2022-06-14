import numpy as np

# [1]
# 记水果名为行号，超市名为列号
# a)
fruits = np.array(["苹果", "香蕉", "桔子", "芒果"])
names = np.array(["大润发", "沃尔玛", "联华", "农工商"])

# b)
price = np.random.random(16)
price = price * 6 + 4
price = price.reshape(4, 4)
print(price)

# c)
price[(fruits == "苹果") | (fruits == "香蕉"), (names == "大润发") | (names == "联华")] += 1
print(price)

# d)
price[:, (names == "农工商")] -= 2
print(price)

# e)
print(price[(fruits == "苹果") | (fruits == "芒果")].mean(axis=1))

# f)
print(names[price[(fruits == "桔子")].argmax()])

# [2]
steps = 10
rndwlk = np.random.normal(0, 1, size=(3, 10))

# rndwlk=np.where(rndwlk>0,1,-1)
position = rndwlk.cumsum(axis=1)
dists = (abs(position[0]) ** 3 + abs(position[1]) ** 3 + abs(position[2]) ** 3) ** (1/3)
print(f"各轴移动距离：{rndwlk}")
print(f"位置：{position}")
z_max=np.max(position[2])
print(f"z轴最大距离：{z_max}")
dists_min=np.min(dists)
print(f"离远点最近距离：{dists_min}")
np.set_printoptions(precision=2)

print(f"距离：{dists}")
