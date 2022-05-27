string1 = input("Please enter a string:")
resoult1 = {}
resoult2 = []
for s in string1:
    resoult1[s] = string1.count(s)
for key in resoult1:
    resoult2.append(f'("{key}",{resoult1[key]})')
print(resoult2)