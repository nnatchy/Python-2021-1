import urllib
import urllib.request as urq
import os

dir_path = os.path.dirname(os.path.realpath("__file__"))
print(dir_path)

url = 'https://comprogchula.github.io/'
html = str(urq.urlopen(url).read().decode('utf-8'))

# ---- TO DO 1 : Code Here ----

count = 0
data = html.splitlines()
for line in data:
    if 'Faculty' in line and '/a' in line:
        a1 = line.find('Faculty')
        a2 = line.find('</a>')
        print(line[a1:a2])
        count+=1
print('Number of Faculties :',count)

##################################################################################################################################################################

# ---- TO DO 2 : Code Here ----

url = 'https://comprogchula.github.io/'
html = str(urq.urlopen(url).read().decode('utf-8'))

data = html.splitlines()
total_img = 0
img = []
for line in data:
    if 'jpg' in line \
        and '1024x640' in line \
            and 'data-srcset' in line:
        a1 = line.find('https')
        a2 = line.find('jpg')
        print(line[a1:a2+3])
        img.append(line[a1:a2+3])
        total_img += 1
print('Total images:',total_img)

for image in img:
    d = urq.urlopen(image)
    l = open('/content/faculty_image/'+str(image[36:]),'wb')
    l.write(d.read())
l.close()

##################################################################################################################################################################

# ---- TO DO 3 : Code Here ----
from urllib.request import urlopen as req
import re

def request(url):
    res = req(url)
    raw = res.read().decode('utf-8')
    res.close()
    return raw

res_html = request("https://www.chula.ac.th/academics/academic-units/faculties-and-schools/")

# --- find faculty websites

urls = []

process = [a for a in res_html.split('<a href="') if "academic/faculty-" in a][::2]

for i in process:
    urls.append(i[:i.find('"')])
    
# --- find their phone numbers

phone_numbers = []

for webUrl in urls:
    res_html = request(webUrl)
    
    t = res_html.split("โทรศัพท์ ")[1]
    fac_number = re.findall("\d\s\d{4}\s\d{4}", t)[0]
    
    phone_numbers.append(fac_number)

# --- output
with open('res', 'w') as f:
    f.write("\n".join(phone_numbers))

#################################################################################################
# ---- TO DO 4 : Code Here ----
url = 'https://www.cp.eng.chula.ac.th/en/about/faculty/'
html = str(urq.urlopen(url).read().decode('utf-8'))

data = html.splitlines()
name = []
for line in data:
    if '</a></p>' in line:
        a = line.split('                                ')
        name.append(a)
name.pop(-1)
names = []
for i in range(len(name)):
    for j in range(len(name[i])):
        names.append(name[i][1])
q = names[0]
real_name = []
real_name.append(names[0])
for i in range(1, len(names)):
    if q != names[i]:
        real_name.append(names[i])
        q = names[i]
    else:
        q = names[i]

list1 = ['DR. PITCHAYA SITTHI-AMORN', 'Assoc. Prof. Dr. Somchai Tayanyong', 'CHUCHEEP SHIMWONG', 'MATEE SRISANGWAN', 'Asst. Prof. Sumet Vacharachaisurapol', 'Asst.Prof. WICHAN LERTWIPATRAKUL', 'CHARUMATR PINTHONG', 'Dr. THIT SIRIBOON', 'Assc.Prof. NONGLUK COVAVISARUCH', 'Dr. CHAIRAT PHONGPHANPHANEE',
         'Assc.Prof. NONGLUK COVAVISARUCH']
for i in real_name:
    if i in list1:
        real_name.remove(i)
real_name.pop(-1)

CurrentF = []
Retired = []
temp = ['Assc.Prof. Dr. SARTID VONGPRADHIP',
        'Assc.Prof. Dr. WANCHAI RIVEPIBOON', 'Assc.Prof. MANDHANA PRAKANSAMUT',
        'Asst.Prof. Dr. SUEBSKUL PHIPHOBMONGKOL', 'Asst.Prof. BOONCHAI SOWANWANICHAKUL',
        'Asst.Prof. Korbkul Tejavanija', 'Asst.Prof. THANAWAN CHANTARATANAPIBUL', 'Dr. YUNYONG TENG-AMNUAY']

for i in real_name:
    if i in temp:
        Retired.append(i)
    else:
        CurrentF.append(i)



Current = []
for i in CurrentF:
    i = i.strip()
    Current.append(i)



print('Current Faculty Members')
print('')
for i in Current:
    print(i)

print('')

print('Retired Faculty Members (Optional)')
print('')
for i in Retired:
    print(i)


########################################################################################################################################################

# Optional DEKD

import urllib
import urllib.request as urq
import os

dir_path = os.path.dirname(os.path.realpath("__file__"))
print(dir_path)

dd_url = 'https://www.dek-d.com/home/writer/'

headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'} 


dd_request = urq.Request(dd_url,None,headers) 
dd_html = str(urq.urlopen(dd_request).read().decode('utf-8'))

data = dd_html.splitlines()
b = []
for line in data:
    if 'class="title"' in line and  'href=' in line \
        and 'style=' not in line and 'view' in line and 'kwang' not in line:
            a = line.find('title=')
            final = line[a+7:-3]
            b.append(final)
b.pop(-1)
#1
for i in range(len(b)):
    print(b[i])
#2
for i in range(len(b)):
    if 'DON&#039;T' in b[i]:
        b[i] = b[i].replace('DON&#039;T',"DON'T")
    print(b[i])
    
            