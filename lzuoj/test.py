a = input()
list1 = []
for i in a:
    list1.append(i)
list1[:] = [int(j)*2 for j in list1]
list1 = list1[::-1]
def jinwei(list1):
    for m in range(len(list1)-1):
        if list1[m] >= 7:
            list1[m+1] = list1[m+1] + 1
            list1[m] = list1[m] - 7
            jinwei(list1)
        else:
            pass
jinwei(list1)
list1 = list1[::-1]
if len(list1)==1:
    list1[0] = (int(list1[0]/7))*10 + list1[0]%7
else:
    num = int((list1[0] + int(list1[1]/7))/7)
    list1[-1] = list1[-1]%7
    if num != 0:
        list1.insert(0,num)
        list1[1] = list1[1]-7
    else:
        pass
list1[:] = [str(n) for n in list1]
print(''.join(list1))