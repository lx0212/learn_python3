class MyClass():
    i = 123
    def f(self,num):
        # print(self.i+num)
        return self.i + num 

x = MyClass()
print(x.f(200))

class Complex:
    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称,
    # 按照惯例它的名称是 self。self 不是 python 关键字
    # self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
    def __init__(self,a,b):
        print("init")
        self.x = a
        self.y = b

c = Complex(11,22)
print(c.x,c.y)

class People:
    name = 'defaultValue'
    age = 0
    #  #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("People:",self.name,self.age,self.__weight)

p = People('lbs',22,100)
p.speak()
# print(p.__weight)

class Student(People):
    grade = ''
    def __init__(self):
        # #调用父类的构函
        People.__init__(self,'userName',23,99)
        self.grade = 111

    def speak(self):
        print("覆写父类的方法:",self.name,self.age,self.grade)

s = Student()
print("---")
s.speak() # 调用覆写父类的方法
super(Student,s).speak() # 用子类对象调用父类已被覆盖的方法。 super() 函数是用于调用父类(超类)的一个方法。
print("---")

class Speaker():
    topic = ''
    name = ''

    def __init__(self,a,b):
        self.topic = a
        self.name = b

    def speak(self):
        print("Speker topic=%s name=%s" % (self.topic,self.name))

# sp = Speaker(11,22)
# sp.speak()

# 多重继承
class Sample(Speaker,Student):
    a = ''
    def __init__(self):
        Student.__init__(self)
        Speaker.__init__(self,66,88)

    def __testPrivate(self):
        print("this is private method")

    def sample(self):
        self.__testPrivate()


sample = Sample()
#方法名同，默认调用的是在括号中参数位置排前父类的方法#方法名同，默认调用的是在括号中参数位置排前父类的方法
sample.speak()
# sample.__testPrivate() # 调用私有方法会报错
sample.sample()



