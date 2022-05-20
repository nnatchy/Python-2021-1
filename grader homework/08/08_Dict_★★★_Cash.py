def total(pocket):
    total = 0
    for key in pocket:
        total += int(key) * int(pocket[key])
    return total

def take(pocket,money_in):
    for key in money_in:
        if key in pocket:
            pocket[key] += money_in[key]
        else:
            pocket[key] = money_in[key]
    return pocket

#7-11 ผิด

def pay(pocket, amt):
    pay = {}
    tempPay = {}
    total = 0
    for key in pocket:
        total += key*pocket[key]
    if amt > total:
        return {}
    for key in sorted(pocket)[::-1]: 
        if amt//key == 0:
            continue
        elif (amt//key) >= pocket[key]:
            tempPay[key] = pocket[key]
            amt = amt - pocket[key]*key
            continue
        tempPay[key] = amt//key
        amt = amt - tempPay[key]*key
    for key in tempPay:
        if tempPay[key] == 0:
            pass
        else:
            pay[key] = tempPay[key]
    else:
        for key in pay:
            pocket[key] -= pay[key]
        return pay
exec(input().strip())