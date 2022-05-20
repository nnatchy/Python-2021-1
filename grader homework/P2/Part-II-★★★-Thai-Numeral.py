def to_Thai(N):
    d = {0:'soon',1:'neung',2:'song',3:'sam',4:'si',5:'ha',6:'hok',7:'chet',8:'paet',9:'kao'}
    out = ''
    if N == 1:
        return 'neung'
    if N >= 1000:
        amt = N//1000
        if N%1000 == 0:
            return d[amt] + ' pun '
        out += d[amt] + ' pun '
        N %= 1000
    if N >= 100:
        amt = N//100
        if N % 100 == 0:
            return out + d[amt] + ' roi '
        out += d[amt] + ' roi '
        N %= 100
    if N >= 10:
        amt = N//10
        if N%10 == 0:
            if d[amt] == 'neung':
                return out + 'sip '
            return out + d[amt] + ' sip '
        if amt == 2:
            out += 'yi ' + 'sip '
        elif amt == 1:
            out += 'sip '
        else:
            out += d[amt] + ' sip '
        N %= 10
    if N >= 0:
        amt = N//1
        if amt == 1:
            out += 'et '
        else:
            out += d[amt]
    return out.strip()   
        
exec(input().strip())