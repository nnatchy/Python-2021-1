M = int(input())
N = int(input())
M = str(M)
if len(M) < N:
    new_ = '0'*(N-len(M)) + str(M)
    print(new_)
else:
    print(M)