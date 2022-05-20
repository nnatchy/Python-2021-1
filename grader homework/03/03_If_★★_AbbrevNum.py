n = int(input())
if n < 1000:
  print(n)
elif n >= 1000 and n < 10000:
  print(str(round(n/1000,1)) + 'K')
elif n >= 10000 and n < 10**6:
  a = n//10
  print(str(round(a/100)) + 'K')
elif n>=10**6 and n < 10**7:
  print(str(round(n/10**6,1)) + 'M')
elif n >= 10**7 and n < 10**9:
  b = n//10000
  print(str(round(b/100)) + 'M')
elif n>=10**9 and n < 10**10:
  print(str(round(n/10**9,1)) + 'B')
elif n >= 10**9:
  c = n//10**7
  print(str(round(c/100)) + 'B')