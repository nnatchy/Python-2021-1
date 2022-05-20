def no_lowercase(t):
    for i in t:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


def no_uppercase(t):
    for i in t:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True


def no_number(t):
    for i in t:
        if i in '1234567890':
            return False
    return True


def no_symbol(t):
    for i in t:
        if i in '!@#$%^&*()_+\"':
            return False
    return True


def character_repetition(t):
    count = 1
    if len(t) == 0:
        pass
    else:
        q = t[0]
        for i in t:
            if i == q:
                count = count + 1
            else:
                q = i
        if count >= 4:
            return True
        return False


def number_sequence(t):
    t = t.lower()
    number = '01234567890'
    for i in range(len(t)-3):
        if t[i:i+4] in number or t[i:i+4] in number[::-1]:
            return True
    return False


def letter_sequence(t):
    t = t.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(t)-3):
        if t[i:i+4] in alpha or t[i:i+4] in alpha[::-1]:
            return True
    return False


def keyboard_pattern(t):
    t = t.lower()
    c1 = '!@#$%^&*()_+'
    c2 = 'qwertyuiop'
    c3 = 'asdfghjkl'
    c4 = 'zxcvbnm'
    for i in range(len(t)-3):
        if t[i:i+4] in c1 or t[i:i+4] in c1[::-1]:
            return True
        elif t[i:i+4] in c2 or t[i:i+4] in c2[::-1]:
            return True
        elif t[i:i+4] in c3 or t[i:i+4] in c3[::-1]:
            return True
        elif t[i:i+4] in c4 or t[i:i+4] in c4[::-1]:
            return True
    return False


# -----------------------------------------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append('No numbers')
if no_symbol(passw):
    errors.append('No symbols')
if character_repetition(passw):
    errors.append('Character repetition')
if number_sequence(passw):
    errors.append('Number sequence')
if letter_sequence(passw):
    errors.append('Letter sequence')
if keyboard_pattern(passw):
    errors.append('Keyboard pattern')
if len(errors) == 0:
    errors.append('OK')
for i in errors:
    print(i)
