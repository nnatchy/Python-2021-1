ticketnumber = []
qfororder = []
waitq = []
timein = []
timefinish = []
avg = []



n = int(input())
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        ticketnumber.append(int(c[1]))
    
    elif c[0] == 'new':
        print('ticket',ticketnumber[-1])
        qfororder.append(ticketnumber[-1])
        ticketnumber.append(ticketnumber[-1]+1)
        timein.append(int(c[1]))
    
    elif c[0] == 'next':
        first = qfororder[0]
        print('call',first)
        waitq.append(first)
        qfororder.pop(0)
        timefinish.append(timein[0])

   #ticketnumber =  #[301,302]
   #qforoder =  #[302]
   #timein = #[1100,1110]
   #timefinish = [1100]
   #avg #[]
    
    elif c[0] == 'order':
        index = ticketnumber.index(waitq[-1])
        wait = int(c[1]) - timein[index]
        print('qtime',waitq[-1],wait)
        waitq.pop(0)
        avg.append(wait)
    
    elif c[0] == 'avg_qtime':
        total = 0
        for i in range(len(avg)):
            total = total + avg[i]
        average = total/len(avg)
        print('avg_qtime',round(average,4))

        

