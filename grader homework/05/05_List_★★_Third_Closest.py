import math
n = int(input())
a = []
for i in range(n):
    k = input().split()
    for j in range(len(k)):
        k[j] = float(k[j])
    a.append(k)
dis = []
for i in range(len(a)):
    for j in range(len(a[i])):
        distance = math.sqrt((a[i][0])**2 + (a[i][1])**2)
    dis.append(distance)
dis1 = sorted(dis)
index = dis.index(dis1[2])
final = a[index]
print('#'+str(index+1)+':'+' '+'('+str(final[0])+',',str(final[1])+')')