class piggybank:
    def __init__(self):
        self.coins = {}
        self.total = 0
        self.totalcoins = 0
   
    def add(self, v, n):
        if self.totalcoins + n <= 100:
            if v in self.coins:
                self.coins[float(v)] += n
            else:
                self.coins[float(v)] = n
            self.totalcoins += n
            self.total = 0
            for i in self.coins:
                self.total += self.coins[i] * i
            return True
        return False
    
    def __int__(self):
        return int(self.total)
    
    def __float__(self):
        return float(self.total)
    
    def __str__(self):
        l = []
        for i in (sorted(self.coins)):
            l.append('%s:%s' %(i,self.coins[i]))
        final = ', '.join(l)
        return '{' + final + '}'
         
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
