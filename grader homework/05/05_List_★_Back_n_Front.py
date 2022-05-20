n = int(input())
l1 = []
for i in range(n):
    num = int(input())
    l1.append(num)
b = input().split()
l2 = []
for i in range(len(b)):
    l2.append(int(b[i]))
l3 = []
while True:
    c = int(input())
    if c == -1:
        break
    l3.append(c)
l = l1 + l2 + l3
final = []
for i in range(len(l)):
    if i%2 == 0:
        final.append(l[i])
    else:
        final.insert(0,l[i])
print(final)
