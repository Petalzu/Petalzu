a = int(input())

def solution(a):
    while a>0:
        b = input()
        if 2022 <= len(b)<= 2022**2:
            print('YES')
        else:
            print('NO')
        a = a-1

solution(a)