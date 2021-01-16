def duplicate_encode(word):
    a = ""
    for x in word.lower():
        if (word.lower().count(x) > 1):
            a += ')'
        else:
            a += '('
    return (a)
