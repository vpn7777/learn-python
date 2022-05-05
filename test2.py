# import math
P = int(input())
X = int(input())
Y = int(input())
cont = (X * 100 + Y) * (100 + P)
print(int(cont // 10000), int((cont/100) % 100))
# if cont2 >= 0.5:
#    print(int(cont), math.ceil(cont2))
# else:
#    print(int(cont), math.floor(cont2))
