
id2money = {}
id2name = {}

for i in range(int(input())):
    inp = input().split()
    name,id,money = inp[0],inp[1],float(inp[2])
    id2money[id] = money
    id2name[id] = name
    
want = input().strip().split()
while want[0] != 'exit':
    if len(want) == 4:
        name,id,cmd,money = want[0],want[1],want[2],float(want[3])
        if cmd == 'deposit':
            if id not in id2money:
                id2money[id] = 0
                id2name[id] = name
            if id2name[id] != name:
                print('Transaction Failed')
            else:
                id2money[id] += money
                if id2money[id] % 1 == 0:
                    id2money[id] = int(id2money[id])
                print('%s (%s)' %(id2name[id],id),str(id2money[id]))
        
        elif cmd == 'withdraw':
            if id not in id2money:
                print('Transaction Failed')
            else:
                if id2name[id] != name:
                    print('Transaction Failed')
                else:
                    if id2money[id] - money < 0:
                        print('Transaction Failed')
                    else:
                        id2money[id] -= money
                        if id2money[id] % 1 == 0:
                            id2money[id] = int(id2money[id])
                        print('%s (%s)' %(id2name[id],id),str(id2money[id]))
    
    elif len(want) == 5:
        name,id,cmd,goto,money = want[0],want[1],want[2],want[3],float(want[4])
        
        if cmd == 'transfer':
            if id not in id2money:
                print('Transaction Failed')
            elif goto not in id2money:
                print('Transaction Failed')
            else:
                if id2name[id] != name:
                    print('Transaction Failed')
                else:
                    if id2money[id] - money < 0:
                        print('Transaction Failed')
                    else:
                        id2money[id] -= money
                        id2money[goto] += money
                        if id2money[id] % 1 == 0:
                            id2money[id] = int(id2money[id])
                        if id2money[goto] % 1 == 0:
                            id2money[goto] = int(id2money[goto])
                        print('%s (%s)' %(id2name[id],id),str(id2money[id]))
                        print('%s (%s)' %(id2name[goto],goto),str(id2money[goto]))
    
    want = input().strip().split()
