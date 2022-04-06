n = int(input())
l_list  = list()
m_list = list()


for i in range(n):
    l_list.append(input())

m = int(input())

for i in range(m):
    m_list.append(int(input())-1)

for i in range(len(l_list)):
    for j in range(len(m_list)):
        if i == m_list[j]:
            print(l_list[i])

