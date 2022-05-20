def change(i):
    i = i.strip()
    j = i.split(',')
    return j

d1 = {}
d2 = {}
inp1 = input()
op1 = open(inp1)
inp2 = input()
op2 = open(inp2)
for line in op1.readlines():
    pol = change(line)
    d1[pol[0]] = pol[1]
for line in op2.readlines():
    pol = change(line)
    d2[pol[0]] = pol[1]
inp3 = input()
op3 = open(inp3)
for line in op3.readlines():
    pol = change(line)
    if pol[0] in d1 and pol[1] in d2:
        print(d1[pol[0]] + ',' + d2[pol[1]])
    else :
        print('record error')