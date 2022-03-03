import math
import random

list = [8,2,3]
list2 = [4,6,9]

print(math.fabs(-10.0)) # 返回数字的绝对值，如math.fabs(-10) 返回10.0
print(math.ceil(4.1)) # 返回数字的上入整数，如math.ceil(4.1) 返回 5
print(math.floor(-4.1)) #返回数字的下舍整数，如math.floor(-4.1)返回 -5
print(math.exp(1)) # 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print(math.log(100,10)) # 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print(max(1,2,3)) # 返回给定参数的最大值，参数可以为序列。
print(min(4,5,6)) #返回给定参数的最小值，参数可以为序列。
modf = math.modf(12.33) # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print(modf)
print(modf[0])
print(modf[1])

print(round(11.49)) # 返回浮点数 x 的四舍五入值
print(math.sqrt(16)) #返回数字x的平方根。

list = [1,2,8,9,13,77,88,66]

print(random.choice(list)) # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。

i = 0
while i < 10:
    print(random.randrange(10,20,2)) # randrange ([start,] stop [,step]) 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
    i+=1

print(random.random()) # 随机生成下一个实数，它在[0,1)范围内。

random.shuffle(list) # 将序列的所有元素随机排序
print(list)

print(random.uniform(10,15)) # 随机生成下一个实数，它在[x,y]范围内。

# 数学常量
print(math.pi)
print(math.e)
