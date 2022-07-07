a = int(input())
b = input().split()
b[:] = [int(i) for i in b]
c = b[0]
b = sorted(b,reverse=True)
d = str(b.index(c) + 1)
if d[-1] == '1':
    print(d+'st')
elif d[-1] == '2':
    print(d+'nd')
elif d[-1] == '3':
    print(d+'rd')
else:
    print(d+'th')