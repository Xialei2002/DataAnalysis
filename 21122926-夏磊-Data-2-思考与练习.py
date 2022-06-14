import numpy as np

subjects = np.array(["Math", "English", "Python", "Chinese", "Art", "Database", "Physics"])
names = np.array(["王徽", "肖良英", "方绮雯", "刘旭阳", "钱易铭"])
scores = np.array([[70, 85, 77, 90, 82, 84, 89], [60, 64, 80, 75, 80, 92, 90], [90, 93, 88, 87, 86, 90, 91], [80, 82, 91, 88, 83, 86, 80], [88, 72, 78, 90, 91, 73, 80]])
# [1]

# 1.1
print(subjects[[1,2,4]])
print(names[-2])
# 1.2
print(names[2:])
print(subjects[2:5])
# 1.3
print(subjects[(subjects == "English") | (subjects == "Physics")])

# 2.1
print(scores[1,4])

# 2.2
print(scores[[2,4]][:,(subjects=="Math")|(subjects=="Python")])

# 2.3
print(scores[:,(subjects=="Math")|(subjects=="Art")])

# 2.4
print(scores[(names=="王徽")|(names=="刘旭阳")][:,(subjects=="English")|(subjects=="Art")])

# 3
arr1=np.ones((1,10),dtype=int)
arr1=arr1*10
for i in range(0,10):
	arr1[:,i]+=i
arr1=arr1.reshape(2,5)
print(arr1)

# [2]
# 1
print(scores-3)

# 2
print(scores.mean(axis=1))

# 3
arr2=np.random.uniform(-1,1,12)
arr2.reshape(3,4)
print(arr2)