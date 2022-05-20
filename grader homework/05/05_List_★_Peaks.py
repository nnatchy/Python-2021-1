n = [float(i) for i in input().split()]
count = 0
for i in range(len(n)-2):
    if n[i+1] > n[i] and n[i+1] > n[i+2]:
        count += 1
print(count)
