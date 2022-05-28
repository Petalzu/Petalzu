list1 = [1,1,2]
def check(list1):
    li2 = set(list1)
    if len(li2) == 1:
        print(3)
    elif len(li2) == 2:
        print(2)
    elif len(li2) == 3:
        print(0)
check(list1)