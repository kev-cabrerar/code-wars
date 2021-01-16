def openOrSenior(data):
    res = []
    for x in data:
        age = x[0]
        handicap = x[1]
    # senior >7 y age >=55
    # print(x[0],x[1])
        if age >= 55 and handicap > 7:
            res.append('Senior')
        else:
            res.append('Open')
    return res
