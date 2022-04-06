n = int(input())
l_list  = list()

for i in range(n):
    l_list.append(int(input()))

a = int(input())
b = int(input())

s1 = l_list[a-1:b:1]
sum = 0

for i in range(len(s1)):
    sum += s1[i]

print(sum)










    

