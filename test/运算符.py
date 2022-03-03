a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b
print("a & b=",bin(c))

c = a | b
print("a | b=",bin(c))

c = a ^ b
print("a ^ b=",bin(c))

c = ~a
print("~a=",c)

c = a << 2
print("a << 2=",bin(c))

c = a >> 2
print("a >> 2=",bin(c))

d = 0
print(bin(~d))

x = 10
y = 20
z = -30
f = False
t = True

print(f and t)  # 与
print(t or f)   # 或
print(not(-1))  # 非

print("-----------------")

a = 10
b = 20
b = 30

print(a is b) # is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等
print(a is not b)

num = 10
if num < 10 or num > 20:
    print("test1")
elif num == 15:
    print("test2")
else:
    print("test3")

if num == 10 : print("test4")


