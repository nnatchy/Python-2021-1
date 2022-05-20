def change(text):
    import string
    upper = (string.ascii_uppercase)*2
    lower = (string.ascii_lowercase)*2
    final = ''
    for ch in text:
        if ch in upper:
            i = upper.find(ch)
            final = final + upper[i+13]
        elif ch in lower:
            i = lower.find(ch)
            final = final + lower[i+13]
        else:
            final = final + ch
    return final
text1 = input()
while text1.strip().lower() != 'end':
    print(change(text1))
    text1 = input()
