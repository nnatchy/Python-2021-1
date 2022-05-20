a = input().split()
num1 = int(a[0],2)
num2 = int(a[1],2)
num = num1+num2
real = bin(num)
print(real[2:])