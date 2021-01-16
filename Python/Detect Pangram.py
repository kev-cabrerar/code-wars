import string


def is_pangram(s):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x''y', 'z']
    c = []
    for x in s.lower():
        if(x in a):
            c.append(x)
    c = (list(set(c)))
    if len(c) == 24:
        return True
    else:
        return False
