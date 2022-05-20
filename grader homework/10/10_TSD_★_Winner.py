w = []
l = []
for i in range(int(input())):
    winner, loser = input().split()
    l.append(loser)
    if winner in l or loser in w:
        if winner in w:
            w.remove(winner)
        elif loser in w:
            w.remove(loser)
    else:
        if winner not in w:
            w.append(winner)
print(sorted(w))