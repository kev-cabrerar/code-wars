def first_non_repeating_letter(string):
    ans = ''
    for o in string:
        if string.lower().count(o.lower()) > 1:
            continue
        else:
            ans = o
            break
    return (ans)
