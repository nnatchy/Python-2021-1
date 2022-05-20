#ข้อมูลนักเรียน
def read_answers(): 
    N = int(input())
    answers = []
    for k in range(N):
        sid, ans = input().split()
        answers.append([sid, ans])
    return answers

#ตรวจ เต็ม 5 ไม่ใช่ร้อยละ
def marking(answer, solution): 
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    return score

#ให้คะเเนน
def grading(score):
    g = [[80,"A"], [70,"B"],\
        [60,"C"], [50,"D"]]
    for a,b in g:
        if score >= a:
            return b
    return "F"

#report
def report(scores):
    for sid,sc,grade in scores:
        print(sid, sc, grade)

#เปลี่ยน marking เป็น % + ขั้นตอน grading
def scoring(answers, solution):
    scores = []
    for sid, ans in answers: #marking
        score = marking(ans, solution) / \
                len(solution) * 100
        grade = grading(score) #grading
        scores.append([sid, score, grade])
    return scores

#เรียงคะเเนน
def sort(scores):
    x = []
    for sid,score,grade in scores:
        x.append([score, sid, grade])
    x.sort()
    for i in range(len(x)):
        scores[i] = [x[i][1], x[i][0], x[i][2]]

key = input()
score = scoring(read_answers(),key)
sort(score)
report(score[::-1])
