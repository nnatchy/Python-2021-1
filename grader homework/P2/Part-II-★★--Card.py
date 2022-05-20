card = input()
card_list = []
dict2 = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'C':1,'D':2,'H':3,'S':4}
l = []
for i in range(0,len(card)-1,2):
    card_list.append(card[i]+card[i+1])
for i in range(len(card_list)-1):
    if card_list[i][0] == card_list[i+1][0]:
        l.append((dict2[card_list[i][1]]-dict2[card_list[i+1][1]]))
    else:
        l.append((dict2[card_list[i][0]]-dict2[card_list[i+1][0]]))
for i in l:
    if i>0:
        print('+%d' %(i),end='')
    else:
        print((i),end='')