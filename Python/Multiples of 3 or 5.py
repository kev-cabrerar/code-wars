def solution(number):
    sum = 0
    for x in range(number):
        # Multiplos de 3 y 5
        if x % 3 == 0 and x % 5 == 0:
            sum += x
        elif x % 3 == 0:
            sum += x
        elif x % 5 == 0:
            sum += x
        x -= 1
    return(sum)
