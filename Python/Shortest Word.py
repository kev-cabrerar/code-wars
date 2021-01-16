def find_short(s):
    # your code here
    data = s.split(" ")
    sw = sorted(data, key=len)
    return (len(sw[0]))
