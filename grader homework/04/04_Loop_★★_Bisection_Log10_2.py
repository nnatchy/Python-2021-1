a = float(input())
L = 0
temp = a
count = 0
while temp != 0:
    temp = temp//10
    count += 1
U = count
x = (L+U)/2
while abs(a-10**x) > 1e-10*max(a,10**x):
    if 10**x > a:
        U = x
        x = (L+U)/2
    else:
        L = x
        x = (L+U)/2
print(round(x,6))





