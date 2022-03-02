# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

list = ['abc',123,11.11,'test','test2']
list2 = [22.3,"test3"]

list[1] = 4556

print(list[0])
print(list[0:2])
print(list * 2) # 输出两次列表
print(list+list2) # 连接列表

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []  # 将对应的元素值设置为 [] 
print(a)

input = 'i like test'
inputList = input.split(" ")
print(inputList)
inputList = inputList[-1::-1]
print(inputList)
