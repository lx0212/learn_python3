from collections import deque
# 将列表当做堆栈使用

stack = [3, 4, 5]
stack.append(7)
stack.append(8)
stack.append(9)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# 将列表当作队列使用
# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；
# 但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，
# 然而在列表里插入或者从头部弹出速度却不快（
# 因为所有其他的元素都得一个一个地移动）

queue = deque(["test1","test2","test3"])
queue.append("test4")
queue.append("test5")

queue.popleft()
print(queue)


vec = [2, 4, 6]
for x in vec:
    print([x,x**2])
 
collect = {"test1":11, "test2":22, "test3":33}

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
for k, v in collect.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
users = ['vv','tt','uu']

for q, a, u in zip(questions,answers,users):
    print("{0} {1} {2}".format(q,a,u))


str = "{}{}testContent".format("123","456")
print(str)


