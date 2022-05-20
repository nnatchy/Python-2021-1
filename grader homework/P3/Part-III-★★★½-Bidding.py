stock = {}
order = []
person = []
for i in range(int(input())):
    inp = input().split()  # B ชื่อคนประมูล รหัสสินค้า dollars
    if inp[0] == 'B':
        if inp[1] not in person:
            person.append(inp[1])
        if inp[2] in stock:
            stock[inp[2]].append([int(inp[3]), inp[1]])
            order.append([i, [inp[2], int(inp[3]), inp[1]]])
        else:
            stock[inp[2]] = [[int(inp[3]), inp[1]]]
            order.append([i, [inp[2], int(inp[3]), inp[1]]])
    elif inp[0] == 'W':
        if inp[2] in stock:
            for j in range(len(stock[inp[2]])):
                if inp[1] in stock[inp[2]][j]:
                    stock[inp[2]][j] = []
for k,v in stock.items():
    temp = []
    for l in v:
        if len(l) != 0:
            temp.append(l)
    stock[k] = temp
person.sort()
store = []
for k, v in sorted(stock.items()):
    v.sort()
    for i in range(len(v)):
        if v[i-1][0] == v[i][0]:
            store.append([k, v[i],v[i][1]])
            break
        elif len(v[i]) == 1:
            store.append([k, v[0],v[0][1]])
        else:
            store.append([k, v[-1],v[-1][1]])
            break
final = {}
for bid in store:
    for i in range(len(bid)):
        if bid[2] not in final:
            final[bid[2]] = bid[1][0]
            break
        else:
            final[bid[2]] += bid[1][0]
            break
for p in person:
    if p not in final:
        final[p] = 0
d = {}
for bid in store:
    if bid[2] not in d:
        d[bid[2]] = [bid[0]]
    else:
        d[bid[2]].append(bid[0])
        d[bid[2]].sort()
for bid in person:
    if bid in d and bid in final:
        print('%s: $%s -> %s' %(bid,final[bid],' '.join(d[bid])))
    else:
         print('%s: $%s' %(bid,final[bid]))