operator = input()
if operator == 'flip':
    number = int(input())
    infor = []
    for i in range(number):
        slot = input().strip()
        infor.append(slot)
    for i in range(len(infor)):
        infor[i] = infor[i][-1::-1]
    for i in infor:
        print(i)
elif operator == '180':
    number = int(input())
    infor = []
    for i in range(number):
        slot = input().strip()
        infor.append(slot)
    for i in range(len(infor)):
        infor[i] = infor[i][-1::-1]
    for i in range(len(infor)-1,-1,-1):
        print(infor[i])
elif operator == '90':
    number = int(input())
    infor = []
    for i in range(number):
        slot = input().strip()
        infor.append(slot)
    loop = len(infor[0])
    ok = []
    check = 0
    for i in range(len(infor)-1):
        if len(infor[i]) != len(infor[i+1]):
            check = 1
    if check == 1:
        print('Invalid size')
    elif check == 0:
        for i in range(loop):
            temp1 = ''
            for j in range(len(infor)):    
                temp = ''
                temp = temp+infor[j][i]
                temp1 = temp1+temp
            ok.append(temp1)
        for i in range(len(ok)):
            ok[i] = ok[i][-1::-1]
            print(ok[i])
        
    

    
