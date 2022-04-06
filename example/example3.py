m = int(input())
all_list = list()
day_list = list()
uniq_list = list()

for i in range(m):
    all_list.append(input().strip())
    
n = int(input())

for i in range(n):
    col = int(input())
    for j in range(col):
        food = input().strip()
        if food in all_list and not(food in day_list):
            day_list.append(food)

for i in all_list:
    if not (i in day_list):
        uniq_list.append(i)

uniq_list.sort()

for i in uniq_list:
    print(i)


