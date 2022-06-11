num1 = input()
def solution(num):
    l = []
    if num == 0:
        print(0)
    else:
        while True:
            num,reminder = divmod(num,3)
            l.append(str(reminder))
            if num == 0:
                print("".join(l[::-1]))
                break
solution(int(num1))

