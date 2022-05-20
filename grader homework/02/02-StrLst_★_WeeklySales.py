a,b,c,d,e,f,g = [int(i) for i in input().split()]
dict = [a,b,c,d,e,f,g]
total = 0
for i in range(len(dict)):
    total += dict[i]
print(total)
