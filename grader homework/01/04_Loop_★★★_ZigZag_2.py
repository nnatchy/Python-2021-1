a = input().split()
b = a
check = True
real_min = 0
real_max = 0
while check == True:
  c = input()
  if c == 'Zig-Zag' or c == 'Zag-Zig':
    break
  else:
    c = c.split(' ')
    b = b+c
for i in range(len(b)):
  b[i] = int(b[i])

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


    

