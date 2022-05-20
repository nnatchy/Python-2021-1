def make_int_list(x):
    l = x.split(' ')
    num = []
    for i in l:
        if i in '/."()[]' or i in "'":
            return num
        elif int(i)%1 == 0:
            num.append(int(i))
        else:
            return num
    return num

def is_odd(e):
    if e%2 == 0:
        return False
    return True

def odd_list(alist):
    l = []
    for i in alist:
        if is_odd(i) == True:
            l.append(i)
    return l

def sum_square(alist):
    total = 0
    for i in alist:
        total = total + i*i
    return total

exec(input().strip())