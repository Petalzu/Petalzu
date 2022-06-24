a = int(input())

def solution(a):
    i = -1
    b = input()
    d = []
    e = [d]
    f = []
    for n in b:
        d.append(n)
    if a == 1:
        if 'B' not in d:
            print(i)
        if 'B' in d:
            print(1)
    else:
        while i<=a:
            c = []
            i = i+1
            for j in range(0,len(d)-1):
                if d[j] == d[j+1]:
                    c.append(1)
                else:
                    c.append(0)
            d = c
            e.append(c)
    for m in e:
        if 1 in m:
            num1 = e.index(m)
            f.append(num1)
    num2 = max(f)
    print(num2 +1)
solution(a)