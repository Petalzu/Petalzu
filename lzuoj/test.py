import numpy as np

a = input().split()
a[:] = [int(i) for i in a]
list1 = []
list2 = []

def inputarray(num):
    i = 0
    while i < num:
        b = input().split()
        b[:] = [int(i) for i in b]
        list1.append(b)
        i = i+1

def change(lists):
    lists = np.array(lists)
    lists = lists.transpose()
    for j in lists:
        j = ' '.join(repr(e) for e in j)
        list2.append(j)
    list2 = ''.join(list2)
    print(list2)

inputarray(a[0])
change(list1)