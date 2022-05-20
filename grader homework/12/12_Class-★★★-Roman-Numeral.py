class roman :
    def __init__(self, r):
        d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        total = d[r[-1]]
        for i in range(len(r)-2,-1,-1): #6,0
            if d[r[i]] >= d[r[i+1]]:
                total += d[r[i]]
            else:
                total -= d[r[i]]
        self.rome = r
        self.num = total
        
    def __lt__(self, rhs):
        return self.num < rhs.num
    def __str__(self):
        return str(self.rome)
                
    def __int__(self):
        return (self.num)
    def __add__(self, rhs):
        d1 = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV': 4}
        d2 = {}
        for key in d1:
            d2[d1[key]] = key
        num = self.num + rhs.num
        l = []
        final = ''
        for i in range(4):
            l.append(((num//10**(3-i))%10) * 10**(3-i))
        for i in l:
            if i >= 1000:
                final += 'M' * int(i//1000)
            elif i >= 100:
                if i in d2:
                    final += d2[i]
                elif i // 100 >= 5:
                    final += 'D' + 'C' * int((i//100)-5)
                elif i // 100 >= 1:
                    final += 'C' * int((i//100))
            elif i >= 10:
                if i in d2:
                    final += d2[i]
                elif i // 10 >= 5:
                    final += 'L' + 'X' * int((i//10)-5)
                elif i // 10 >= 1:
                    final += 'X' * int((i//10))
            elif i >= 1:
                if i in d2:
                    final += d2[i]
                elif i // 1 >= 5:
                    final += 'V' + 'I' * int((i)-5)
                elif i // 1 >= 1:
                    final += 'I' * int((i))
        return roman(final)
        
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))