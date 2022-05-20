n = input()
k = n[3::7]
l = n[7::5]
total = int(k) + int(l) +10**4
total = str(total)
#เอาหลัก พัน ร้อย สิบ only
#ปัญหาตอนนี้คือมีหลักเเสนโผล่ด้วย
new_ = total[-2:-5:-1]
new_ = new_[::-1]
b = int(new_)
c = b//100 #8
d = b%10   #3
e = b//10  #81
f = e%10   #1
sum_ = 0
sum_ = c+d+f
#5
newone = sum_%10
last = newone + 1
list = ['A','B','C','D','E','F','G','H','I','J']
last = last - 1
print(str(new_) + list[last])