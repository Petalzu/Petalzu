string1 = input("Please enter a string:")
resoult1 = {}
resoult2 = {" "}
for s in string1:
    resoult1[s] = string1.count(s)
for key in resoult1:
    resoult2.add(f'"{key}":{resoult1[key]}')
resoult2.remove(" ")
print(resoult2)