n = int(input())
l = []
for i in range(n):
    s = set([int(i) for i in input().split()])
    l.append(s)
if n == 0:
    print(0)
    print(0)
else:
    k = set();k1 = l[0]
    for i in range(len(l)):
        k = k | l[i]
        k1 = k1 & l[i]
    print(len(k))
    print(len(k1))