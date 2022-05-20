filename = input().strip()
cmd = input().strip()
if cmd not in ['LSTRIP', 'RSTRIP', 'STRIP', 'STRIP_ALL']:
    print('Invalid command')
    exit(0)

# ตรวจความถูกต้องของ cmd ถ้าผิดก็แสดงข้อความ Invalid command
# แล้วใช้คำสั่ง exit(0) เพื่อจบโปรแกรมได้เลย

# ???


# อ่านแต่ละบรรทัดในแฟ้มมาเพื่อหาความกว้างของช่องว่างทางขอบซ้ายและขอบขวา
fn = open(filename)
left_margin = 99999         # ให้ช่องว่างทางขอบซ้ายมีค่ามาก ๆ ไว้ก่อน
right_margin = 99999

for line in fn:
    line = line.strip()
    # นับจำนวนจุดใน line เริ่มจากขอบซ้ายไปทางขวา หยุดนับเมื่อพบตัวที่ไม่ใช่จุด เก็บในตัวแปร left
    # เช่น ถ้า line = "....|...|.." จะได้ left มีค่า 4
    for left in range(len(line)):
        if line[left] != '.':
            break
    if left < left_margin:
        left_margin = left

    # ทำในทำนองเดียวกัน เพื่อหาค่า right_margin
    for right in range(len(line)):
        if line[-right] != '.':
            break
    if right < right_margin:
        right_margin = right

fn.close()

if cmd != 'STRIP_ALL':
    # LSTRIP, RSTRIP  หรือ STRIP
    # เปิดแฟ้มใหม่เพื่ออ่านข้อมูลอีกรอบ  รอบนี้ อ่านแต่ละบรรทัดมา เพื่อตัดจุดที่ขอบซ้ายและ/หรือขอบขวา ตามคำสั่งแสดง แล้วก็แสดงเลย

    fn = open(filename)

    # ???  จัดการกรณี LSTRIP, RSTRIP และ STRIP
    if cmd == 'LSTRIP':
        for line in fn.readlines():
            line = line.strip()
            print(line[left_margin:])
        fn.close()

    elif cmd == 'RSTRIP':
        for line in fn.readlines():
            line = line.strip()
            print(line[:-right_margin+1])
        fn.close()

    elif cmd == 'STRIP':
        for line in fn.readlines():
            line = line.strip()
            print(line[left_margin:-right_margin+1])
        fn.close()

else:
    # STRIP_ALL
    import numpy as np

    fn = open(filename)
    
    l = []
    for line in fn.readlines(): 
        line = line.strip()
        selected = line[left_margin:-right_margin+1]
        k = []
        for i in selected:
            k.append(i)
        l.append(k)
    id = []
    A = np.array(l,str)
    for i in range(A.shape[1]):
        check = True
        for j in A[:, i]:
            if j != '.':
                check = False
        if check == True:
            id.append(int(i))
    c = 0
    for i in id:
        A = np.delete(A, i-c, 1)
        c += 1
    ans = A.tolist()
    for i in ans:
        print(''.join(i))

    # ???  ตรงนี้ซับซ้อน ค่อยทำทีหลัง (มี testcases แค่ประมาณ  20% ของทั้งหมด)

    fn.close()
