def bouncingBall(h, bounce, window):
    count = 0
    if(h > 0 and bounce > 0 and bounce < 1 and window < h):
        count += 1
    else:
        return -1
    h = h*bounce
    while(h > window):
        count += 2
        h = h*bounce
    return count
