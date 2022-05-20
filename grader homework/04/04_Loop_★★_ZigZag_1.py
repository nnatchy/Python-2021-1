n = int(input())
a = []
for i in range(n):
    a.append(i for i in input().split())
b = []
for i in range(len(a)):
    for j in a[i]:
        b.append(int(j))
c = input()
if c == 'Zig-Zag':  
    l1 = b[0]
    r1 = b[3]
    minn1 = l1
    minn2 = r1
    check = False
    for i in range(0,len(b),4):
      if b[i] < minn1:
        minn1 = b[i]
    for i in range(3,len(b),4):
      if b[i] < minn2:
        minn2 = b[i]
    if minn1 < minn2:
      real_min = minn1
    else:
      real_min = minn2
    r2 = b[1]
    l2 = b[2]
    maxx1 = r2
    maxx2 = l2
    for i in range(1,len(b),4):
      if b[i] > maxx1:
        maxx1 = b[i]
    for i in range(2,len(b),4):
      if b[i] > maxx2:
        maxx2 = b[i]
    if maxx1 > maxx2:
      real_max = maxx1
    else:
      real_max = maxx2

elif c == 'Zag-Zig':
    l1 = b[0]
    r1 = b[3]
    maxx1 = l1
    maxx2 = r1
    for i in range(0,len(b),4):
      if b[i] > maxx1:
        maxx1 = b[i]
    for i in range(3,len(b),4):
      if b[i] > maxx2:
        maxx2 = b[i]
    if maxx1 > maxx2:
      real_max = maxx1
    else:
      real_max = maxx2
    r2 = b[1]
    l2 = b[2]
    minn1 = r2
    minn2 = l2
    for i in range(1,len(b),4):
      if b[i] < minn1:
        minn1 = b[i]
    for i in range(2,len(b),4):
      if b[i] < minn2:
        minn2 = b[i]
    if minn1 < minn2:
      real_min = minn1
    else:
      real_min = minn2
print(real_min,real_max)