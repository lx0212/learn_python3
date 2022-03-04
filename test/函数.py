
def max(a,b):
    if a > b:
        return a
    else:
        return b

def hello():
    print("hello")

# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
def changeList(param):
    param[0] = 111
    print(param)

# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
def changeNum(params):
    print(id(params))
    param = 22
    print(id(params))

def printme(name,age):
    print("name=%s" % name)
    print("age=%d" % age)

# 调用函数时，如果没有传递参数，则会使用默认参数
def printinfo(name,age = 33):
    print("name=%s" % name)
    print("age=%d" % age)

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def funcname(arg1,*vartuple):
    print(arg1)
    print(vartuple)

# 加了两个星号 ** 的参数会以字典的形式导入。
def funcname2(arg1,**vardict):
    print(arg1)
    print(vardict)

def myfunc(n):
  return lambda a : a * n

def funcnone(n):
    print(n)
    return

print(max(1,2))
hello()

list = [3,4,6,8,0]
changeList(list)
print(list)

a = 66
changeNum(a)
print(id(a))
print(a)

# 使用关键字参数允许函数调用时参数的顺序与声明时不一致
printme(age = 12, name = "testName")

printinfo("testName2")

tuple = (1,2,3)
tuple2 = (4,5,6)

# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数
funcname(70,tuple,tuple2,66)

funcname2(1,a=2,b= "testb")

# 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
x = lambda a,b : a+b
print(x(10,11))


 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))
print(myfunc(5)(11))
print(funcnone(3))
