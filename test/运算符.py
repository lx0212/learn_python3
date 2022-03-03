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
