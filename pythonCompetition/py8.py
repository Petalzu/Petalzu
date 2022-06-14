a = int(input())
b = list(map(int,input().split()))


list1 = []
list2 = []
list3 = []
list4 = []
def solution(a):
    while a>0:
        c = input(list(map(int,input().split())))
        b.append(b[0])
        b.remove(b[0])
        list3.append(b)
        a = a+1
    list1 = set(list1)
    for j in list3:
        for i in range(0,a):
            num = i * j[i]
            list2.append(num)
            num2 = sum(list2)
            list4.append(num2)
    print(min(list4))
solution(a)