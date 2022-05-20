sentence = input().lower()
data = []
for i in range(int(input())):
    data.append(input().strip())
data.sort(key=len,reverse = True)
left = sentence
ans = ''
dataid = {}
for word in data:
    if word in left:
        index = left.index(word)
        left = left.replace(word, ' '*len(word))
        dataid[word] = [index, index+len(word)]
dataid = {k: v for k, v in sorted(dataid.items(), key=lambda item: item[1])}
c = 0
for i in dataid:
    start, end = dataid[i]
    sentence = sentence[:start+c]+' '+sentence[start+c:end+c]+' '+sentence[end+c:]
    c += 2
sentence = sentence.split()
for i in range(len(sentence)):
    sentence[i] = sentence[i].strip()
print(' '.join(sentence))