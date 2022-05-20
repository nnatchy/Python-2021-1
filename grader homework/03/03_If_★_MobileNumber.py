n = input()
list1 = ['06','08','09']
if len(n) == 10:
    if n[0:2] not in list1:
        print('Not a mobile number')
    elif n[2::] in list1:
        print('Not a mobile number')
    else:
        print('Mobile number')
else:
    print('Not a mobile number')
