from ast import Num
from audioop import avg
from re import I
from tkinter import N

i = 1
i = int(i)
studentnum = []
SG1 = []
SG2 = []
Avg = []

while True:
    if i < 5:
        student1 = input("Student "+str(i)+" number:")
        studentnum.append(student1)
        S1G1 = input("Student " + str(student1)+" grade 1: ")
        SG1.append(str(S1G1))
        S2G2 = input("Student " + str(student1)+" grade 2: ")
        SG2.append(str(S2G2))
        avg1 = (int(S1G1) + int(S2G2))/2
        Avg.append[avg1]
        i = i +1
    else:
        break

print("Number  Grade 1  Grade 2  Avg")
print(studentnum[0]+SG1[0]+SG2[0]+Avg[0])
print(studentnum[1]+SG1[1]+SG2[1]+Avg[1])
print(studentnum[2]+SG1[2]+SG2[2]+Avg[2])
print(studentnum[3]+SG1[3]+SG2[3]+Avg[3])
