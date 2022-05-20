n = input()
n12 = (11-(13*int(n[0]) + 12*int(n[1])+11*int(n[2])+10*int(n[3])+9*int(n[4])+8*int(n[5])+7*int(n[6])+6*int(n[7])+5*int(n[8])+4*int(n[9])+3*int(n[10])+2*int(n[11]))%11)%10
a = n[0]
b = n[1:5]
c = n[5:10]
d = n[10:12]
print(a + ' '+b + ' '+c+' '+d+' '+str(n12))