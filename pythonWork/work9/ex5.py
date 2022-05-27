list1 = [1,11,5,5]
list2 = list1
k = 16
for i in list1:
    for j in list2:
        if i + j == k:
            print(str(i)+'+'+str(j)+'='+str(k))
    else:
        pass