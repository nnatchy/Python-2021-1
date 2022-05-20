val = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
st = ['club','diamond','heart','spade']

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'
    
    def next1(self):
        if self.suit == 'spade':
            if self.value == '2':
                nval = '3'
            else:
                nval = val[val.index(self.value)+ 1]
            ns = 'club'
        else:
            ns = st[st.index(self.suit)+1]
            nval = self.value
        return Card(nval,ns)
            
    
    def next2(self):
        a = self.next1()
        self.value = a.value
        self.suit = a.suit

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])