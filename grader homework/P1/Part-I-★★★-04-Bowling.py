result = input().strip()
target = int(input())
total = 0
rnd = 0
round = []
ind = 0 
k = 100
num = ['0','1','2','3','4','5','6','7','8','9','10']
wantin = ['1','2','3','4','5','6','7','8','9','10']
for i in range(len(result)): #-3+1
    if k <= 10:
        k = 100
        ind += 1
        continue
    else:
        if rnd == 9:
            if len(result[i:]) == 3:
                if result[i] == 'X':
                    if result[i+1] == 'X':
                        if result[i+2] == 'X':
                            k = 30
                            total += k
                            round.append([ind,k])
                            break
                        else:
                            k = 20 + int(result[i+2])
                            total += k
                            round.append([ind,k])
                            break
                    elif result[i+1] in num:
                        if result[i+2] == '/':
                            k = 20
                            total += k
                            round.append([ind,k])
                            break
                        elif result[i+2] in num:
                            k = 10 + int(result[i+1]) + int(result[i+2])
                            total += k
                            round.append([ind,k])
                            break
                elif result[i+1] == '/':
                    if result[i+2] in num:
                        k = 10 + int(result[i+2])
                        total += k
                        round.append([ind,k])
                        break
                    elif result[i+2] == 'X':
                        k = 20
                        total += k
                        round.append([ind,k])
                        break
            elif len(result[i:]) == 2:
                k = int(result[i]) + int(result[i+1])
                total += k
                round.append([ind,k])
                break
        else:
            if result[i] == 'X':
                if result[i+2] == '/':
                    k = 20
                    total += k
                    rnd += 1
                    round.append([ind,k])         
                elif result[i+1] == 'X':
                    if result[i+2] == 'X':
                        k = 30
                        total += k
                        rnd += 1
                        round.append([ind,k])             
                    elif result[i+2] in num:
                        k = 20 + int(result[i+2])
                        total += k
                        rnd += 1
                        round.append([ind,k])
                elif result[i+1] in num:
                    if result[i+2] in num:
                        k = 10 + int(result[i+1]) + int(result[i+2])
                        total += k
                        rnd += 1
                        round.append([ind,k])
                    elif result[i+2] == '/':
                        k = 20
                        total += k
                        rnd += 1
                        round.append([ind,k])                
            elif result[i] == '/':
                ind += 1
                continue
            elif result[i] in num:
                if result[i+1] == '/':
                    if result[i+2] in num:
                        k = 10 + int(result[i+2])
                        total += k
                        rnd += 1
                        round.append([ind,k])
                    else:
                        k = 20
                        total += k
                        rnd += 1
                        round.append([ind,k])
                elif result[i+1] in num:               
                    if result[i+2] == '/':
                        ind += 1
                        continue
                    else:
                        k = int(result[i]) + int(result[i+1])
                        total += k
                        rnd += 1
                        round.append([ind,k])
    ind += 1
if str(target) not in wantin:
    print(total)
else:
    for i in range(len(round)):
        if target-1 == i:
            print(round[i][1])
            

        

        
            
            
    
            
     
    
