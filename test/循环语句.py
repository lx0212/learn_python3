
# while

a = 1

while a < 10:
    print(a)
    a += 1
    if a == 8: break
else:
    print("while else")

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []

while len(numbers) > 0:
    number = numbers.pop()

    if number%2:
        even.append(number)
    else:
        odd.append(number)

print("even=",even)
print("odd=",odd)

# for

for letter in 'Python':
    print("当前字母:%s",letter)

item = ['a','b','c','d']

for i in item:
    print("i=%s" % i)

# 通过序列索引迭代
for index in range (len(item)):
    print(item[index])

print("----------")

for num in range (10,20):
    print(num)

for num in range (10,20):
    for i in range (2,num):
        if num % i == 0:
            break
    else:
        print("%d 是质数" % num)

print("-------test--------")

i = 97
j = 2
while(j <= (i/j)):
    print("i=%d j=%d (i/j)=%f" % (i,j,(i/j)))
    j+=1
    
# 打印0-10的奇数
n = 0
while n < 10:
    n+=1
    if not(n % 2):continue
    print(n)




