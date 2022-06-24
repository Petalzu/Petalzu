a = int(input())

def solution(a):
    i = -1
    b = input()
    d = list(b)
    if a == 1:
        if 'B' not in d:
            print(-1)
        if 'B' in d:
            print(1)
    else:
        if set(d)==1:
            print(len(d))
        else:
            while i<=a:
                c = []
                i = i+1
                if 1 in d:
                    for j in range(0,len(d)-1):
                        if d[j] == d[j+1]:
                            c.append(1)
                        else:
                            c.append(0)
                    d = c
                else:
                    if len(d)>1:
                        if len(set(d)) ==1:
                            print(i+int(len(d)))
                            break
                        else:
                            pass
                    else:
                        print(i)
                        break
solution(a)




