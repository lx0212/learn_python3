word1 = "test1"
word2 = "test2"
word3 = """test1,test2
test3
test4
"""
print(word1)
print(word2)
print(word3)

print("------------")

str = "123456789"

print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[1:5:2]) # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)
print(str + "hello")
print("test1\ntest2")
print(r"test1\ntest2") # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
