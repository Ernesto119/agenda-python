a = 9119
l =[]
# for x in str(a):
#     c = int(x)**2
#     l.append(str(c))
# print("".join(l))



print(int("".join([str(int(x)**2) for x in str(a)])))