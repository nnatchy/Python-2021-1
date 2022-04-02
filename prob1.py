week = int(input())
if week <= 2:
    print('No results')
else:
    l = []
    for i in range(week):
        stuff = input().split(',')
        for j in stuff:
            l.append(float(j))
    # Fast EMA = 7 วัน , slow = 14 วัน

    def fastEMA(l):
        period = 7
        back = []
        total = 0
        for i in range(0, period):
            total += l[i]
        back.append([l[6], total/period])
        for i in range(period, len(l)):
            temp = 0
            alpha = 2/(1+period)
            temp = (alpha*l[i]) + back[i-period][1]*(1-alpha)
            back.append([l[i], temp])
        return back

    def slowEMA(l):
        period = 14
        back = []
        total = 0
        for i in range(0, period):
            total += l[i]
        back.append([l[13], total/period])
        for i in range(period, len(l)):
            temp = 0
            alpha = 2/(1+period)
            temp = (alpha*l[i]) + back[i-period][1]*(1-alpha)
            back.append([l[i], temp])
        return back

    slow = slowEMA(l)
    fast = fastEMA(l)[7:]

    check = []
    for i in range(len(slow)):
        if fast[i][1] < slow[i][1]:
            check.append(True)
        elif fast[i][1] > slow[i][1]:
            check.append(False)
        else:
            check.append('1')
            
    #False = buy #True = sell
    
    final = []
    for i in range(len(check)-1):
        if check[i] != check[i+1]:
            if check[i] == True and check[i+1] == False:
                final.append(['BUY',i+1])
            elif check[i] == False and check[i+1] == True:
                final.append(['SELL',i+1])
    if len(final) > 0:
        for i in range(len(final)):
            print('%s at %s' %(final[i][0],'{:.2f}'.format(fast[final[i][1]][0])))
    else:
        print('No results')
                
        
        
