n = input()
c = [0]*len(n)
for i in range(len(n)):
    if '(' == n[i]:
        c[i] = '['
    elif '[' == n[i]:
        c[i] = '('
    elif ')' == n[i]:
        c[i] = ']'
    elif ']' == n[i]:
        c[i] = ')'
    else:
        c[i] = n[i]
k = ''
for i in range(len(c)):
    k += c[i]
print(k)

