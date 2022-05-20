import math
n = input().split(',')
num = str(n[0]) + '.' + str(n[1]) #7.4(str)
num = float(num) #7.4(float)
l_sed = int(num*10**(len(n[1])))
l_suan = 10**(len(n[1]))
temp = int(n[2])# 81 
r_suan = (10**len(n[2])-1)*10**(len(n[1])) #ส่วนตัวสอง
r_sed = temp
sed = l_sed*r_suan + r_sed*l_suan
suan = l_suan*r_suan
gcd = math.gcd(sed,suan)
a = int(sed//gcd)
b = int(suan//gcd)
print(a,'/',b)