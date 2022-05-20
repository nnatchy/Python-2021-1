# txt = ''
# for line in open(input(),'r'):
#     txt += line.strip() +'.'
# k = int(input())
# ruler = ''
# for i in range(k//10):
#     ruler += '-'*9 + str(i+1)
# if k%10 != 0:
#     ruler += '-'*(k%10)
# st = ''
# word = ''
# print(ruler)
# for i in range(len(txt)):
#     st += txt[i]
#     if txt[i] == '.' and txt[i-1] != '.':
#         word += st
#         st = ''
#     if len(word.strip('.')) + len(st) >= len(ruler):
#         print(word.strip('.'))
#         word = ''
# print(word.strip('.'))

class A: 
    def __init__(self, a, b):
        self.s = [a,b]
    def __str__(self):
        return ':'.join([(' '+str(e))[-2:] for e in self.s])
    def f(self):
        return A(self.s[1],self.s[0])

a1 = A(9,1)
a2 = a1.f()
a3 = a2.f()
print(a1)
print(a2)
print(a3)