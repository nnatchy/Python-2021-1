import numpy as np

def read_data():
    # อ่านข ้อมูลจากแป้นพิมพ์ จากนั้นสร้างและคืนอาเรย์สองตัว
    # weight เป็นอาเรยส์ ามชอ่ งเก็บน ้าหนักของคะแนนกลางภาค ปลายภาค และโครงงาน (float)
    # data เป็นอาเรย์ขนาด n4 เก็บข ้อมูลนักเรียน n คน แต่ละคนมีข ้อมูล
    # เลขประจ าตัว คะแนนกลางภาค ปลายภาค และโครงงาน (int)
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight,data):
    wtdata = weight * data[:,1:]
    sumwtdata = np.sum(wtdata,axis = 1)
    #print(sumwtdata,np.mean(sumwtdata))
    finaldata = data[sumwtdata < np.mean(sumwtdata)][:,0]
    if finaldata.shape[0] != 0:
        print((', '.join([str(i) for i in finaldata])))
    else:
        print('None')
        
exec(input().strip()) 