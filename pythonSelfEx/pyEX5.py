import random
theChosen = []

for i in range(0,2):
    j = random.randint(2,148)
    theChosen.append(j)

print(set(theChosen))