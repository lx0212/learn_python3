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

#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple = ('abc', 123, 11.22, 'test1')

print(tuple)

tuple1 = (3,) # 一个元素，需要在元素后添加逗号
print(tuple1[0])

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
tuple2 = ('test1',list)
list[0] = 'ddd'
print(tuple2)

sites = {'Google', 'Taobao', 'Facebook', 'Baidu','Tabobao'}
print(sites)

a = set("test123")
b = set("test4567")
print(a - b) # a 和 b 的差集(从a中减掉相同的元素)
print(a | b)


dict = {}
dict['one'] = "this is one"
dict[3] = "this is three"
dict[4] = 4567
print(dict['one'])
print(dict[3])
print(dict[4])
print (dict)
print(dict.keys())  # 输出所有键
print(dict.values()) # 输出所有值

dict2 = {'name':"username", 'age':11, 3:5}
print(dict2)


print(int('12',16))  # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制

print("------list method------")
list = [2, 5, 7, 88, 4 ,5, 66, 2, 1, 5, 4, 66]
list2 = [33,44,55]

list.append(88) # 在列表末尾添加新的对象
print(list.count(5)) # 统计某个元素在列表中出现的次数
list.extend(list2) # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(list.index(5)) # 从列表中找出某个值第一个匹配项的索引位置
list.insert(2,8) # list.insert(index, obj) 将对象插入列表
list.pop(2) # list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(5) # 移除列表中某个值的第一个匹配项
list.reverse() # 反向列表中元素
list.sort() # 对原列表进行排序
list2 = list.copy() # 复制列表
list.clear() # 清空列表

print(list)
print(list2)



