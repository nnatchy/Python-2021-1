class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'
        
    def getScore(self):
        role = ['J','Q','K']
        if self.value in role:
            value = 10
        elif self.value == 'A':
            value = 1
        else:
            value = int(self.value)
        return value
    
    def sum(self,other):
        return (self.getScore() + other.getScore())%10
        
    def __lt__(self,rhs):
        if self.value != rhs.value:
            if self.value == '2' :
                val = 'Z'
            elif self.value == 'A':
                val = 'Y'
            elif self.value == 'K':
                val = 'X'
            elif self.value == 'Q':
                val = 'W'
            elif self.value == 'J':
                val = 'V'
            elif self.value == '10':
                val = 'U'
            else :
                val = self.value
            
            if rhs.value == '2' :
                rv = 'Z'
            elif rhs.value == 'A':
                rv = 'Y'
            elif rhs.value == 'K':
                rv = 'X'
            elif rhs.value == 'Q':
                rv = 'W'
            elif rhs.value == 'J':
                rv = 'V'
            elif rhs.value == '10':
                rv = 'U'
            else :
                rv = rhs.value
            return val < rv
        return self.suit < rhs.suit
        
     
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].getScore())
print("----------")
for i in range(n-1):
 print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
 print(cards[i])