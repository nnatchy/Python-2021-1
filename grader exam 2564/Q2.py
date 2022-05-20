def ratingcal(level,score):
    return int(25*(level+1)*(score/10**7))

d = {}

n = int(input())
for i in range(n):
    inp = input().split(' | ')
    
    if inp[0] == 'Play' and len(inp) == 4:
        song = inp[1]
        level = int(inp[2])
        score = int(inp[3])
        
        if song not in d:
            d[song] = [level,score,ratingcal(level,score)]
        else:
            
            if ratingcal(level,score) > d[song][2]:
                d[song] = [level,score,ratingcal(level,score)]
            
            elif d[song][2] == ratingcal(level,score):
                
                if d[song][0] == level:
                    
                    if score > d[song][1]:
                        d[song] = [level,score,ratingcal(level,score)]
                
                elif level > d[song][0]:
                    d[song] = [level,score,ratingcal(level,score)]
    
    elif inp[0] == 'Rating' and len(inp) == 1:
        if len(d) <= 5:
            total = 0
            for i in d:
                total += d[i][2]
            print(total)
        else:
            l = []
            for i in d:
                l.append(d[i][2])
            print(sum(sorted(l,reverse=True)[:5]))
    elif inp[0] == 'Rating' and len(inp) == 2:
        song = inp[1]
        if song not in d:
            print('0')
        else:
            print(d[song][2])
    
    elif inp[0] == 'Detail' and len(inp) == 2:
        song = inp[1]
        if song in d:
            print(song,'|',str(d[song][0]),'|',str(d[song][1]),'|',str(d[song][2]))
        else:
            print('%s: No play history' %(song))
                    