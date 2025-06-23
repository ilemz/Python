import random

list = []
list2 = []

for i in range(43):
    list.append(i+1)

print list

max = 43
for i in range(7):
    a = random.randint(1,max)
    max = max-1
    list2.append(list[a])
    del(list[a])

print list2
