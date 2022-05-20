h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
ds = s2-s1
dm = m2-m1
dh = h2-h1
if dm < 0:
  dh = int((23+dh)%24)
  dm = (60+dm)%60
if ds < 0:
  dm = int((59+dm)%60)
  if dm == 59:
    dh = dh-1
ds = (60+ds)%60
dh = (24+dh)%24
print(str(dh) + ":" + str(dm) + ":" + str(ds))