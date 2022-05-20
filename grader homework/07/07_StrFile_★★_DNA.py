def checkDNA(dna):
    code = ['A','T','C','G']
    for i in dna:
        if i not in code:
            return False
    return True

def R(dna):
    code = ['A','T','C','G']
    revcode = ['T','A','G','C']
    output = ''
    for i in dna:
        output += revcode[code.index(i)]
    return output[::-1]

def F(dna):
    code = ['A','T','G','C']
    count = [0]*4
    for i in dna:
        count[code.index(i)] += 1
    return ('A=%d, T=%d, G=%d, C=%d') %(count[0],count[1],count[2],count[3])

def D(dna):
    code = ['A','T','C','G']
    koo = input().strip().upper()
    count = 0
    for i in range(len(dna)-1):
        if dna[i:i+2] == koo:
            count += 1
    return count

dna = input().strip().upper()
op = input().strip().upper()
code = ['A','T','G','C']

if checkDNA(dna) == True:
    if op == 'R':
        print(R(dna))
    elif op == 'F':
        print(F(dna))
    elif op == 'D':
        print(D(dna))
else:
    print('Invalid DNA')
