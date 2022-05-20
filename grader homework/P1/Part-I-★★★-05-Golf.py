b = []
for i in range(9):
    a = input().split()
    b.append(a)
to_par = 0
to_stroke = 0
to_strokefixed = 0
for i in range(len(b)):
    to_par = to_par + int(b[i][0])
    to_stroke = to_stroke + int(b[i][1])
    if b[i][2] == '1':
        if int(b[i][1]) < int(b[i][0]) + 2:
            to_strokefixed += int(b[i][1])
        else:
            to_strokefixed += int(b[i][0]) + 2
    else:
        pass

taem_tor = (0.8*(1.5*to_strokefixed - to_par))//1
final = to_stroke - taem_tor
print(to_stroke)
print(int(taem_tor))
print(int(final))
