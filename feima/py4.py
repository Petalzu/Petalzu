import itertools
a = int(input())

def solution(a):
    while a>0:
        b = input().lower()
        counts(b)
        a = a-1

def dell(t):
    s = []
    for i in t:
        if i =='d':
            s.append(i)
        elif i =='o':
            s.append(i)
        elif i =='g':
            s.append(i)
        else:
            pass
    t = s

def counts(s):
    num1=0
    num2=0
    t = []
    for m in s:
        t.append(m)
    dell(t)
    c = list(itertools.combinations(s, 3))
    for j in c:
        d = ''.join(j)
        if d == 'dog':
            num1 = num1 +1
        elif d == 'god':
            num2 = num2 +1
        else:
            pass
    print(str(num2)+' '+str(num1))
solution(a)