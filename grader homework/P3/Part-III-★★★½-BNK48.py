inp = input().split()
score = {}
voter = {}
topscore = {}
fav = []
while inp[0] not in '123':
    if inp[1] not in fav:
        fav.append(inp[1])
    if inp[1] not in score:
        score[inp[1]] = int(inp[2])
    else:
        score[inp[1]] += int(inp[2])
    if inp[1] not in voter:
        voter[inp[1]] = {inp[0]}
    else:
        voter[inp[1]].add(inp[0])
    if inp[0] not in topscore:
        topscore[inp[0]] = [[int(inp[2]),inp[1]]]
    else:
        topscore[inp[0]].append([int(inp[2]),inp[1]])
    inp = input().split()
if inp[0] in '1':
    print(", ".join([e[0] for e in [[k, v] for k, v in sorted(score.items(),key = lambda obj:obj[1])][::-1][:3]]))
elif inp[0] in '2':
    print(", ".join([e[0] for e in sorted([[k, len(voter[k])] for k in voter], key=lambda obj: obj[1])][::-1][:3]))
elif inp[0] in '3':
    d = {}
    for k,v in sorted(topscore.items()):
        v = sorted(v)[::-1]
        for i in range(len(v)-1):
            if v[i][0] == v[i+1][0]:
                v = sorted(v,key = lambda obj:obj[1])
        if v[0][1] not in d:
            d[v[0][1]] = 1
        else:
            d[v[0][1]] += 1
        if len(d) < 3:
            for i in fav:
                if i not in d:
                    d[i] = 0
    print(", ".join([e[0] for e in [[k, v] for k, v in sorted(d.items(),key = lambda obj:obj[1])][::-1][:3]]))
    
            