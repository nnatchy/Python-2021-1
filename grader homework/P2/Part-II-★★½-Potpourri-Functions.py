import string
def convex_polygon_area(p):
    lx = []
    ly = []
    for i in p:
        for j in range(len(i)):
            if j%2 == 0:
                lx.append(i[j])
            else:
                ly.append(i[j])
    totaladd = 0
    totalmin = 0
    for i in range(len(lx)-1):
        totaladd += lx[i] * ly[i+1]
        totalmin += lx[i+1] * ly[i]
    totaladd += lx[-1] * ly[0]
    totalmin += lx[0] * ly[-1] 
    finalres = 0.5*(totaladd-totalmin)
    return abs(finalres)

def is_heterogram(s):
    d = {}
    st = ''
    for i in s:
        if i in string.ascii_letters:
            st += i
    for i in st.lower():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key in d:
        if d[key] != 1:
            return False
    return True

def replace_ignorecase(s, a, b):
    st = ''
    i = 0
    while i < len(s):
        temp = s[i:i+len(a)]
        if temp.lower() == a.lower():
            st += b
            i += len(a)
        else:
            st += s[i]
            i += 1
    return st

def top3(votes):
    l = []
    for name,score in votes.items():
        l.append([-score,name])
    return [i[1] for i in sorted(l)[:3]]
    
for k in range(2):
    exec(input().strip())
