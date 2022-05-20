from string import ascii_lowercase


def text2keys(text):
    d = {' ': '0', 'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44',\
         'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',\
              's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999'}
    output = ''
    for i in text.lower():
        if i in d or i == ' ':
            output += d[i]+' '
    return output.strip()

def keys2text(keys):
    d = {' ': '0', 'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44',
     'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
     's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999'}
    d1 = {}
    for key in d:
        d1[d[key]] = key
    output = ''
    text = keys.split()
    for i in text:
        output += d1[i]
    return (output.strip())

exec(input().strip())