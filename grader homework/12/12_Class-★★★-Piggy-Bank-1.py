class piggybank:
    def __init__(self):
    # มีตัวแปร 4 ตัวเก็บจ านวนเหรียญของเหรียญแต่ละแบบ
        self.ten = 0
        self.five = 0
        self.two = 0
        self.one = 0
        self.total = 0
    def add1(self, n):
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญบาท
        self.one += n
        self.total = self.ten*10 + self.five*5 + self.two*2 + self.one*1
    def add2(self, n):
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสองบาท
        self.two += n
        self.total = self.ten*10 + self.five*5 + self.two*2 + self.one*1
    def add5(self, n):
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญห้าบาท
        self.five += n
        self.total = self.ten*10 + self.five*5 + self.two*2 + self.one*1
    def add10(self, n):
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสิบบาท
        self.ten += n
        self.total = self.ten*10 + self.five*5 + self.two*2 + self.one*1
    def __int__(self):
    # คืนมูลค่ารวม = ค่าของเหรียญคูณกับจ านวนเหรียญ
        self.total = self.ten*10 + self.five*5 + self.two*2 + self.one*1
        return self.total
    def __lt__(self, rhs):
    # เปรียบเทียบจ านวนเงินใน self กับจ านวนเงินใน rhs
        return self.total < rhs.total
    def __str__(self):
    # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
        d = "{1:%d, 2:%d, 5:%d, 10:%d}" %(self.one,self.two,self.five,self.ten)
        return d
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)